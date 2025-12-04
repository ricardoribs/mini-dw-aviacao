import os
import logging
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carrega as senhas do arquivo .env
load_dotenv()

# Configura o log para avisar se der erro
logging.basicConfig(
    filename='../logs/etl_process.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def get_db_engine():
    # Cria a string de conexão
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    dbname = os.getenv('DB_NAME')
    
    url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    return create_engine(url)