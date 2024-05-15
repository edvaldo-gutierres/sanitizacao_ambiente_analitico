# Importa Bibliotecas
import pandas as pd

# Importa módulos
from controllers.tables_sanitization_controller import (
    list_table_sanitization,
    create_schema_dbthanos,
)
from controllers.env_controller import EnvironmentController


def lista_tabelas(data_base: str) -> pd.DataFrame:
    return list_table_sanitization(data_base=data_base)


def criar_schemas_no_dbthanos(df: pd.DataFrame) -> None:
    for schema_name in df[
        "create_schema"
    ].unique():  # DataFrame com os schemas a serem criados no [dbthanos]
        create_schema_dbthanos(schema_name=schema_name)  # Cria os schemas no [dbthanos]


def criar_tabelas_no_dbthanos(df: pd.DataFrame) -> None:
    # Implemente a lógica para criar tabelas no DBTHANOS
    pass


def insert_tabelas_no_dbthanos(df: pd.DataFrame) -> None:
    # Implemente a lógica para insert de dados nas tabelas no DBTHANOS
    pass


def drop_tabelas_origem(df: pd.DataFrame) -> None:
    # Implemente a lógica para dropar as tabelas do banco de origem
    pass


def registra_processo_sanitizacao(df: pd.DataFrame) -> None:
    # Registra o processo de sanitização para contabilização
    pass


def envia_notificacao() -> None:
    # Envia notificação de sanitização da tabela
    pass


def main():

    # Carrega as variáveis de ambiente
    env_vars = EnvironmentController.load_environment_variables()
    database = env_vars["database"]

    # Cria DataFrame com as informações das tabelas a serem sanitizadas
    table_sanit_data = lista_tabelas(data_base=database)
    df_table_sanit = pd.DataFrame(table_sanit_data)
    df_table_sanit["create_schema"] = (
        df_table_sanit["database_name"] + "_" + df_table_sanit["schema_name"]
    )

    ######################### CRIAR SCHEMA NO [dbthanos] #########################
    criar_schemas_no_dbthanos(df_table_sanit)

    ######################### CRIAR TABELA NO [dbthanos] #########################
    criar_tabelas_no_dbthanos(df_table_sanit)


if __name__ == "__main__":
    main()
