# Importa bibliotecas Python
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError, SQLAlchemyError
import pandas as pd
from datetime import datetime

# Importa modulos
from service.database import DatabaseService

# Informa nome da tabela de log
tab_log = 'dw_hml.data_engineer.tab_log_sanitization'

# Função para listar tabelas elegíveis para sanitização
def list_table_sanitization(data_base: str) -> pd.DataFrame:
    """
    Retorna um DataFrame do Pandas contendo informações sobre tabelas que precisam ser sanitizadas.

    Returns:
        DataFrame: Um DataFrame contendo as seguintes colunas:
            - id
            - server_name
            - database_name
            - schema_name
            - table_name
            - total_row_count
            - table_create_date
            - min_date_report
            - max_date_report
            - qty_days
            - row_ingestion_timestamp
    """

    try:
        # Criar uma instância de DatabaseService
        db_service = DatabaseService()

        # Chamar o método get_session na instância criada
        session = db_service.get_session()

        # Executar o comando USE
        session.execute(text(f"USE {data_base}"))

        # Usar a sessão para executar a consulta
        cursor = session.execute(
            text(
                f"""
            SELECT
                id
                ,server_name
                , database_name
                , schema_name
                , table_name
                , total_row_count
                , table_create_date
                , min_date_report
                , max_date_report
                , qty_days
                , row_ingestion_timestamp
            FROM data_engineer.tab_analytical_tables_sanitization
            WHERE 1 = 1
                AND qty_days > 60
            """
            )
        )

        results = []

        for row in cursor.fetchall():
            result = {
                "id": row[0],
                "server_name": row[1],
                "database_name": row[2],
                "schema_name": row[3],
                "table_name": row[4],
                "total_row_count": row[5],
                "table_create_date": row[6],
                "min_date_report": row[7],
                "max_date_report": row[8],
                "qty_days": row[9],
                "row_ingestion_timestamp": row[10],
            }
            results.append(result)

        # Fecha a sessão
        session.close()

        # Cria um DataFrame
        df = pd.DataFrame(results)

        # Retorna um DataFrame
        return df

    except ProgrammingError as err:
        print(f"Erro ao listar as tabelas para sanitização: {err}")



def write_log_sanitization(tab_log: str, ddl_type: str, database_name: str, schema_name: str, table_name: str) -> None:
    """
    Grava um log de sanitização na tabela especificada.

    Parâmetros:
    tab_log (str): Nome da tabela de log.
    ddl_type (str): Tipo de operação DDL (Data Definition Language).
    database_name (str): Nome do banco de dados.
    schema_name (str): Nome do esquema.
    table_name (str): Nome da tabela.
    row_process_timestamp (datetime): Timestamp do processo de linha.

    Retorna:
    None
    """
    try:
        # Criar uma instância de DatabaseService
        db_service = DatabaseService()

        # Chamar o método get_session na instância criada
        session = db_service.get_session()

        # Executar o comando USE
        session.execute(text(f"USE {database_name}"))

        # Inserir os dados na tabela de log
        session.execute(
            text(f"INSERT INTO {tab_log} (ddl_type, database_name, schema_name, table_name, row_process_timestamp) "
                 "VALUES (:ddl_type, :database_name, :schema_name, :table_name, :row_process_timestamp)"),
            {
                'ddl_type': ddl_type,
                'database_name': database_name,
                'schema_name': schema_name,
                'table_name': table_name,
                'row_process_timestamp': datetime.now()
            }
        )

        # Fazer o commit da transação
        session.commit()
       
    except SQLAlchemyError as err:
        # Capturar e imprimir erros de programação
        print(f"Houve um erro ao gravar o log: {err}")
    
    finally:
        # Garantir que a sessão seja fechada
        session.close()



# Função para criar schema no banco dbthanos
def create_schema_dbthanos(schema_name: str) -> None:
    """
    Cria um novo schema no banco de dados dbthanos, se ele ainda não existir.

    Args:
        schema_name (str): Nome do schema a ser criado.

    Returns:
        None
    """
    try:
        # Criar uma instância de DatabaseService
        db_service = DatabaseService()

        # Chamar o método get_session na instância criada
        session = db_service.get_session()

        # Executar o comando USE
        session.execute(text(f"USE dbthanos"))

        # Verifica se o schema existe
        cursor = session.execute(
            text(
                f"""
                SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{schema_name}'
                """
            )
        )

        schema_exists = cursor.fetchone()[0] > 0

        # Se o schema não existir, cria o schema
        if not schema_exists:
            session.execute(text(f"CREATE SCHEMA {schema_name}"))
            session.commit()
            print(f"Schema '{schema_name}' criado com sucesso.")
        else:
            print(f"Schema '{schema_name}' já existe.")

        # Fecha a conexão
        session.close()

    except ProgrammingError as err:
        if "There is already an object named" in str(err):
            print(f"Schema '{schema_name}' já existe.")
        else:
            print(f"Houve um erro ao tentar criar o schema no banco de dados: {err}")
    



# Função para criar tabelas no banco dbthanos
def create_table_dbthanos(old_db: str, new_db: str, schema_name: str, table_name: str ) -> None:
    """
    Função para criar tabelas no banco dbthanos.

    Esta função copia uma tabela existente de um banco de dados e esquema de origem para o banco de dados de sanitização.
    
    Parâmetros:
    old_db (str): Nome do banco de dados antigo.
    new_db (str): Nome do novo banco de dados.
    old_schema (str): Nome do esquema antigo.
    schema_name (str): Nome do novo esquema.
    table_name (str): Nome da tabela a ser copiada.
    """
    try:
        # Criar uma instância de DatabaseService
        db_service = DatabaseService()

        # Chamar o método get_session na instância criada
        session = db_service.get_session()

        # Executar o comando USE
        session.execute(text(f"USE {new_db}"))

        # Executa o INSERT 
        cursor = session.execute(text(
            f"SELECT * INTO {new_db}.{old_db}_{schema_name}.{table_name} FROM {old_db}.{schema_name}.{table_name}"
        ))

        # Fazer o commit da transação
        session.commit()

        # Grava log
        write_log_sanitization(
            tab_log=tab_log, 
            ddl_type='insert', 
            database_name=new_db, 
            schema_name=f"{old_db}_{schema_name}", 
            table_name=table_name, )
       
    except SQLAlchemyError as err:
        # Capturar e imprimir erros de programação
        print(f"Houve um erro ao tentar criar a tabela no banco de dados: {err}")
    
    finally:
        # Garantir que a sessão seja fechada
        session.close()



# Função para excluir tabelas do banco de dados de origem
def drop_table_origin(database: str, schema_name: str, table_name: str ) -> None:
    """
    Função para excluir tabelas elegíveis ao processo de sanitização.

    Esta função exclui a tabela elegível ao processo de sanitização do banco de dados.
    
    Parâmetros:
    database (str): Nome do banco de dados.
    schema_name (str): Nome do esquema.
    table_name (str): Nome da tabela.

    """
    try:
        # Criar uma instância de DatabaseService
        db_service = DatabaseService()

        # Chamar o método get_session na instância criada
        session = db_service.get_session()

        # Executar o comando USE
        session.execute(text(f"USE {database}"))

        # Executa DROP TABLE
        cursor = session.execute(text(
            f"DROP TABLE {database}.{schema_name}.{table_name}"
        ))

        # Fazer o commit da transação
        session.commit()

        # Grava log
        write_log_sanitization(
            tab_log=tab_log, 
            ddl_type='drop', 
            database_name=database, 
            schema_name=schema_name, 
            table_name=table_name
            )
       
    except SQLAlchemyError as err:
        # Capturar e imprimir erros de programação
        print(f"Houve um erro ao tentar excluir a tabela do banco de dados: {err}")
    
    finally:
        # Garantir que a sessão seja fechada
        session.close()

