import pandas as pd
import glob
import os
from config import get_db_engine

def run_etl():
    print("Iniciando ETL...")
    engine = get_db_engine()
    
    # 1. Ler o arquivo mais recente da pasta RAW
    list_of_files = glob.glob('../data/raw/*.csv')
    if not list_of_files:
        print("Nenhum arquivo encontrado.")
        return
        
    latest_file = max(list_of_files, key=os.path.getctime)
    print(f"Processando arquivo: {latest_file}")
    df = pd.read_csv(latest_file)
    
    # 2. Carregar Dimensões (Tabelas auxiliares)
    # Companhias
    cias = df[['cia_aerea']].drop_duplicates().rename(columns={'cia_aerea': 'codigo_iata'})
    cias['nome_companhia'] = cias['codigo_iata']
    cias['pais_origem'] = 'Brasil'
    
    # Usamos try/except para ignorar erros de duplicação simples
    try:
        cias.to_sql('dim_companhia', engine, if_exists='append', index=False, method='multi')
    except:
        pass # Ignora se já existir (simplificado para iniciante)

    print("Dimensões processadas.")

    # 3. Preparar e Carregar Fatos (Tabela principal)
    # Buscamos o ID que o banco gerou para a companhia
    df_db_cias = pd.read_sql("SELECT id_companhia, codigo_iata FROM dim_companhia", engine)
    
    # Juntamos o CSV com os IDs do banco
    df_final = df.merge(df_db_cias, left_on='cia_aerea', right_on='codigo_iata')
    
    # Prepara colunas para inserir
    tabela_fato = df_final[[
        'id_voo', 'id_companhia', 'data_partida_prevista', 
        'atraso_minutos', 'cancelado', 'motivo_atraso', 
        'condicao_climatica'
    ]].rename(columns={
        'id_voo': 'id_operacao', 
        'data_partida_prevista': 'data_partida'
    })
    
    # Inserir na tabela fato
    try:
        tabela_fato.to_sql('fato_operacoes', engine, if_exists='append', index=False)
        print("Dados carregados no Banco de Dados com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir fato: {e}")

if __name__ == "__main__":
    run_etl()