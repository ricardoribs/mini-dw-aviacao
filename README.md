# ✈️ Mini Data Warehouse de Aviação

Este projeto é uma simulação completa de um ambiente de Engenharia de Dados ("End-to-End"), focado em ingestão, processamento e análise de dados operacionais de companhias aéreas brasileiras.

O objetivo foi construir um **Data Warehouse** do zero para responder perguntas de negócio sobre pontualidade, ocupação de aeronaves e impacto climático nas operações.

## 🛠 Tecnologias Utilizadas
- **Linguagem:** Python 3.12
- **Banco de Dados:** PostgreSQL 16
- **Bibliotecas:** Pandas, SQLAlchemy, Faker, Matplotlib, Seaborn
- **Ferramentas:** VS Code, Jupyter Notebook, pgAdmin 4

## 🏗 Arquitetura do Projeto

O pipeline segue uma arquitetura em camadas (ETL):
1.  **Source (Gerador):** Script Python que cria dados sintéticos realistas de voos, simulando atrasos baseados em condições climáticas.
2.  **Raw/Landing:** Os dados são salvos inicialmente em arquivos CSV.
3.  **ETL (Load):** Script de ingestão que lê os arquivos, valida tipos de dados e carrega para o PostgreSQL.
4.  **Warehouse:** Modelagem **Star Schema** (Esquema Estrela) com tabelas Fato e Dimensões.
5.  **Analytics:** Views SQL para KPIs e Dashboards em Python.

### Modelagem de Dados (Star Schema)
- **Fato:** `fato_operacoes` (Voos, atrasos, ocupação)
- **Dimensões:** `dim_companhia`, `dim_aeronave`, `dim_aeroporto`

## 📊 Resultados e Análises

### 1. Ranking de Pontualidade
Análise via SQL identificando qual companhia aérea teve menor média de atraso.
![Ranking SQL](caminho_para_sua_imagem_do_select_count_ou_ranking.png)

### 2. Impacto do Clima nos Atrasos
Visualização gerada no Jupyter Notebook comprovando a correlação entre condições climáticas adversas e tempo de atraso.
![Gráfico Clima](2.png)

### 3. Distribuição de Atrasos
Histograma analisando a frequência de atrasos por companhia.
![Histograma](3.png)

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.x instalado
- PostgreSQL instalado e rodando
- Criar um banco de dados chamado `dw_aviacao`

### Instalação
1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/mini-dw-aviacao.git](https://github.com/SEU-USUARIO/mini-dw-aviacao.git)
   
2. Instale as dependências:
   pip install pandas sqlalchemy psycopg2-binary python-dotenv faker matplotlib seaborn

3. Configure o arquivo .env com suas credenciais do banco:
   DB_HOST=localhost
DB_NAME=dw_aviacao
DB_USER=postgres
DB_PASS=sua_senha

Execução
   1. Gerar Dados: python src/generate_data.py
   2. Rodar ETL: python src/dw_loader.py
   3. Analisar: Abra o notebook em notebooks/analise_dados.ipynb ou execute as queries na pasta sql/
