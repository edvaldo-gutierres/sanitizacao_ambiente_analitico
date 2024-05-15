from service.database import DatabaseService
from models import tables_sanitization as TableSanit
from sqlalchemy import text

import pandas as pd


def list_table_sanitization() -> pd.DataFrame:
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

        # Usar a sessão para executar a consulta
        cursor = session.execute(
            text(
                """
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
            FROM dw_hml.data_engineer.tab_analytical_tables_sanitization
            WHERE 1 = 1
                AND qty_days > 60;
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

    except Exception as err:
        print(f"Erro ao listar as tabelas para sanitização: {err}")
