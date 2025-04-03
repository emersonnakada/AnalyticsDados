
import pandas as pd
import logging
from datetime import datetime
from plugins.databases.engines.dbkombi import DBK as DBKOMBI
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import psycopg2

# Pegando as configurações do banco destino no .env
load_dotenv("dags/projects/etl_extracao_api_frete/src/.env")

# Configuração do diretório de log
log_directory = "dags/projects/etl_extracao_api_frete/logs"
os.makedirs(log_directory, exist_ok=True)

log_file = os.path.join(log_directory, "etl_log.log")

# Criar um logger
logger = logging.getLogger()

# Remover manipuladores existentes para evitar logs duplicados
if logger.hasHandlers():
    logger.handlers.clear()

logger.setLevel(logging.INFO)

# Criar um manipulador de arquivo
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.INFO)

# Criar um manipulador de console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Definir o formato do log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Adicionar apenas os manipuladores necessários
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logging.info("Teste de log: logging inicializado corretamente.")

# Configuração do banco de destino
DB_MTMFS = {
    "host": os.getenv("MCFPS_HOST_PS"),
    "port": os.getenv("MCFPS_PORT_PS")or "5432",
    "database": os.getenv("MCFPS_NAME_PS"),
    "user": os.getenv("MCFPS_USER_PS"),
    "password": os.getenv("MCFPS_PASSWORD_PS")
}


# Criar engine para o PostgreSQL
DW_CLOUD_ENGINE = create_engine(
    f"postgresql://{DB_MTMFS['user']}:{DB_MTMFS['password']}@{DB_MTMFS['host']}:{DB_MTMFS['port']}/{DB_MTMFS['database']}"
)

def check_connection(engine):
    """Verifica se a conexão com o banco está ativa."""
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        logging.info("Conexão com o banco de dados bem-sucedida.")
        return True
    except Exception as e:
        logging.error(f"Erro na conexão com o banco: {e}")
        return False

def ensure_schema_exists(engine, schema_name):
    """Garante que o esquema existe no PostgreSQL."""
    try:
        with engine.connect() as conn:
            conn.execute(f'CREATE SCHEMA IF NOT EXISTS "{schema_name}";')  
        logging.info(f"Esquema {schema_name} garantido no PostgreSQL.")
    except Exception as e:
        logging.error(f"Erro ao garantir o esquema {schema_name}: {e}")

def list_tables():
    """Lista tabelas do SQL Server"""
    try:
        query = """
        SELECT TABLE_NAME 
        FROM [aldocalculofreteprazoservice].INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_SCHEMA = 'dbo' 
        AND TABLE_TYPE = 'BASE TABLE';
        """
        df = pd.read_sql(query, DBKOMBI.engine)
        logging.info("Listagem de tabelas realizada com sucesso.")
        return df
    except Exception as e:
        logging.error(f"Erro ao listar tabelas: {e}")
        return None

def extract_data(table_name):
    """Extrai os dados de uma tabela específica."""
    try:
        query = f'SELECT * FROM [aldocalculofreteprazoservice].dbo.[{table_name}];'
        df = pd.read_sql(query, DBKOMBI.engine)

        if df.empty:
            logging.warning(f"Tabela {table_name} não retornou dados!")
        else:
            logging.info(f"Extração bem-sucedida: {len(df)} registros extraídos da tabela {table_name}.")
        
        return df
    except Exception as e:
        logging.error(f"Erro ao extrair dados da tabela {table_name}: {e}")
        raise 
    
def transform_data(df):
    """Transforma os dados adicionando a coluna dt_processamento."""
    try:
        logging.info("Iniciando transformação de dados.")
        if df is not None:
            df.drop_duplicates(inplace=True)
            df.fillna('', inplace=True)
            df['dt_processamento'] = pd.to_datetime(datetime.now())
        logging.info("Transformação concluída.")
        return df
    except Exception as e:
        logging.error(f"Erro na transformação de dados: {e}")
        return None

def truncate_table(table_name):
    "truncar tabela, a fim  de respeitar chaves e configurações da tabela de origem"
     
    query = f'TRUNCATE TABLE public.{table_name};'
    
    return query
    

def load_data(df, table_name):
    """Carrega os dados transformados no PostgreSQL."""
    try:
        ensure_schema_exists(DW_CLOUD_ENGINE, "aldocalculofreteprazoservice")  # Garantindo o esquema no PostgreSQL
        
        table_name = table_name.lower()  

        with DW_CLOUD_ENGINE.begin() as conn:
            
            
            conn.execute(text(truncate_table(table_name)))
            df.to_sql(table_name, con=conn, if_exists="append", index=False, schema="public") 

        logging.info(f"Carga de dados da tabela {table_name} concluída com sucesso no PostgreSQL.")

    except Exception as e:
        logging.error(f"Erro ao carregar dados da tabela {table_name}: {e}")
        raise  # Para o processo completamente

# Execução do ETL
if __name__ == "__main__":
    logging.info("Iniciando processo ETL.")

    if check_connection(DBKOMBI.engine):
        tabelas_df = list_tables()
        if tabelas_df is not None:
            for _, row in tabelas_df.iterrows():
                tabela = row["TABLE_NAME"]
                logging.info(f"Processando tabela: {tabela}")

                df = extract_data(tabela)
                if df is not None and not df.empty:
                    df = transform_data(df)
                    if df is not None:
                        load_data(df, tabela)
                else:
                    logging.warning(f"Tabela {tabela} está vazia ou não pôde ser extraída.")
        else:
            logging.error("Erro ao listar as tabelas do banco.")
    else:
        logging.error("Erro na conexão com o banco de dados.")
