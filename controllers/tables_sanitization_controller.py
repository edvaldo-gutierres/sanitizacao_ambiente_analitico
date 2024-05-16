# Importa bibliotecas Python
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError, SQLAlchemyError
import pandas as pd

# Importa modulos
from service.database import DatabaseService


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


# Função para criar o script do create da tabela origem
def get_create_table_origin(data_base: str, table_name: str) -> str:
    """
    Gera o script de criação da tabela do banco de dados origem no dbthanos.

    Args:
        data_base (str): Nome do banco de dados.
        table_name (str): Nome da tabela.

    Returns:
        str: Script de criação da tabela.
    """

    try:
        # Criar uma instância de DatabaseService
        db_service = DatabaseService()

        # Chamar o método get_session na instância criada
        session = db_service.get_session()

        # Executar o comando USE
        session.execute(text(f"USE {data_base}"))

        cursor = session.execute(
            text(
                f"""
                DECLARE @tabela VARCHAR(200);
                SET @tabela = '{table_name}'

                SET NOCOUNT ON

                DECLARE @Create_Table TABLE(s VARCHAR(1000), id INT IDENTITY)

                INSERT INTO  @Create_Table(s) VALUES ('CREATE TABLE ' + @Tabela + ' (')

                INSERT INTO @Create_Table(s)
                SELECT
                    '['+column_name+'] ' + 
                    data_type + 
                    CASE WHEN RTrim(data_type) = 'image' THEN ''
                    ELSE coalesce('('+cast(character_maximum_length AS VARCHAR)+')','') END + 
                    ' ' +
                    CASE WHEN EXISTS ( 
                        SELECT id FROM syscolumns
                        WHERE object_name(id)=@Tabela
                        AND name=column_name
                        AND columnproperty(id,name,'IsIdentity') = 1 
                    ) THEN
                        'IDENTITY(' + 
                        cast(ident_seed(@Tabela) AS VARCHAR) + ',' + 
                        cast(ident_incr(@Tabela) AS VARCHAR) + ')'
                    ELSE ''
                    END + ' ' +
                    ( CASE WHEN IS_NULLABLE = 'No' OR RTrim(column_name) = 'R_E_C_N_O_' THEN 'NOT ' ELSE '' END ) + 'NULL ' + 
                    coalesce('DEFAULT '+COLUMN_DEFAULT,'') + ','
                
                FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = @Tabela
                ORDER BY ordinal_position

                DECLARE @PKName varchar(100)
                SELECT @PKName = constraint_name FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
                WHERE table_name = @Tabela AND constraint_type='PRIMARY KEY'

                IF ( @PKName is not null ) BEGIN
                    INSERT INTO @Create_Table(s) values('  PRIMARY KEY (')
                    INSERT INTO @Create_Table(s)
                        SELECT '   ['+COLUMN_NAME+'],' FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                        WHERE constraint_name = @PKName
                        ORDER BY ordinal_position

                    UPDATE @Create_Table SET s=left(s,len(s)-1) WHERE id=@@identity
                    INSERT INTO @Create_Table(s) VALUES (' )')
                END
                ELSE BEGIN
                    UPDATE @Create_Table set s=left(s,len(s)-1) WHERE id=@@identity
                END

                INSERT INTO @Create_Table(s) values( ')' )

                SELECT * FROM @Create_Table
                """
            )
        )

        # Concatena as linhas em uma string
        result_string = ""
        for row in cursor.fetchall():
            # print(row)
            if row[0] is not None:
                result_string += row[0]

        # Fecha a conexão
        session.close()

        return result_string

    except SQLAlchemyError as err:
        return f"Houve um erro ao tentar gerar o script de criação da tabela no banco de dados origem: {err}"


# Função para criar tabelas no banco dbthanos
def create_table_dbthanos(schema_name: str) -> None:
    try:
        # Criar uma instância de DatabaseService
        db_service = DatabaseService()

        # Chamar o método get_session na instância criada
        session = db_service.get_session()

        # Executar o comando USE
        session.execute(text(f"USE dbthanos"))

        # Verificar se a tabela existe
        cursor = session.execute(text())

    except ProgrammingError as err:
        print(f"Houve um erro ao tentar criar a tabela no banco de dados: {err}")


# Função para Dropar tabela origem
# 1. Verifica se tabela foi criada no dbthanos
# 2. Verifica se quantidade de linhas estão batendo (EXCEPT)
