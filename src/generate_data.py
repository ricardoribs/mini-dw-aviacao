import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime
import uuid
import os

fake = Faker('pt_BR')

def generate_aviation_data(num_records=2000):
    print(f"Gerando {num_records} linhas de dados...")
    
    # Dados básicos
    aeroportos = [
        {'code': 'GRU', 'city': 'Guarulhos', 'uf': 'SP'},
        {'code': 'GIG', 'city': 'Rio de Janeiro', 'uf': 'RJ'},
        {'code': 'BSB', 'city': 'Brasília', 'uf': 'DF'}
    ]
    cias = ['LATAM', 'GOL', 'AZUL']
    
    data = []
    
    for _ in range(num_records):
        # Cria um voo aleatório
        origem, destino = random.sample(aeroportos, 2)
        cia = random.choice(cias)
        
        # Simula atraso baseado em "sorte"
        atraso = 0
        cancelado = False
        clima = np.random.choice(['Sol', 'Chuva', 'Tempestade'], p=[0.7, 0.2, 0.1])
        
        if clima == 'Tempestade':
            atraso = random.randint(30, 200)
            if random.random() < 0.2: cancelado = True # 20% chance cancelar
        
        record = {
            'id_voo': str(uuid.uuid4()),
            'cia_aerea': cia,
            'matricula_aeronave': f"PT-{fake.bothify(text='???').upper()}",
            'modelo_aeronave': 'Boeing 737',
            'capacidade': 180,
            'origem_code': origem['code'],
            'origem_cidade': origem['city'],
            'origem_uf': origem['uf'],
            'destino_code': destino['code'],
            'destino_cidade': destino['city'],
            'destino_uf': destino['uf'],
            'data_partida_prevista': fake.date_time_between(start_date='-1y', end_date='now'),
            'atraso_minutos': atraso,
            'cancelado': cancelado,
            'motivo_atraso': 'Clima' if atraso > 0 else 'Pontual',
            'condicao_climatica': clima,
            'passageiros_embarcados': random.randint(100, 180)
        }
        data.append(record)
        
    df = pd.DataFrame(data)
    
    # Salva na pasta RAW
    # Garante que o diretório existe
    os.makedirs('../data/raw', exist_ok=True)
    filename = f"../data/raw/voos_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
    df.to_csv(filename, index=False)
    print(f"Arquivo salvo em: {filename}")

if __name__ == "__main__":
    generate_aviation_data()