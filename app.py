# Importa Bibliotecas
import pandas as pd

# Importa módulos
from controllers.env_controller import EnvironmentController
from controllers.tables_sanitization_controller import (
    list_table_sanitization,
    create_schema_dbthanos,
    create_table_dbthanos,
    drop_table_origin,
)
from controllers.notification_controller import send_notification


def lista_tabelas(data_base: str) -> pd.DataFrame:
    return list_table_sanitization(data_base=data_base)


def criar_schemas_no_dbthanos(df: pd.DataFrame) -> None:
    for schema_name in df[
        "create_schema"
    ].unique():  # DataFrame com os schemas a serem criados no [dbthanos]
        print(f"Processando criação do schema no dbthanos: {schema_name}")
        create_schema_dbthanos(schema_name=schema_name)  # Cria os schemas no [dbthanos]


def criar_tabelas_no_dbthanos(df: pd.DataFrame, target_db: str) -> None:
    # Implemente a lógica para criar tabelas no DBTHANOS
    for index, row in df.iterrows():
        print(
            f'Processando criação da Tabela no [dbthanos]: {row["database_name"]}.{row["schema_name"]}.{row["table_name"]}'
        )
        create_table_dbthanos(
            old_db=row["database_name"],
            new_db=target_db,
            schema_name=row["schema_name"],
            table_name=row["table_name"],
        )


def drop_tabelas_origem(df: pd.DataFrame) -> None:
    # Implemente a lógica para dropar as tabelas do banco de origem
    for index, row in df.iterrows():
        print(
            f"Processando exclusão da Tabela: {row['database_name']}.{row['schema_name']}.{row['table_name']}"
        )
        drop_table_origin(
            database=row["database_name"],
            schema_name=row["schema_name"],
            table_name=row["table_name"],
        )


def envia_notificacao(destinatario: str, assunto: str, lista_tabelas: list) -> None:
    # Implemente a lógica para enviar notificação
    send_notification(
        destinatario=destinatario, assunto=assunto, lista_tabelas=lista_tabelas
    )


def main():

    # Carrega as variáveis de ambiente
    # env_vars = EnvironmentController.load_environment_variables()
    # database = env_vars["database"]
    database = "dw_hml"
    database_sanit = "dbthanos"

    # Cria DataFrame com as informações das tabelas a serem sanitizadas
    table_sanit_data = lista_tabelas(data_base=database)
    df_table_sanit = pd.DataFrame(table_sanit_data)
    # print(df_table_sanit)
    df_table_sanit["create_schema"] = (
        df_table_sanit["database_name"] + "_" + df_table_sanit["schema_name"]
    )

    try:
        ######################### CRIAR SCHEMA NO [dbthanos] #########################
        criar_schemas_no_dbthanos(df_table_sanit)

        ######################### CRIAR TABELA NO [dbthanos] #########################
        criar_tabelas_no_dbthanos(df=df_table_sanit, target_db=database_sanit)

        ######################### EXCLUI TABELA ELEGÍVEL À SANITIZAÇÃO ###############
        drop_tabelas_origem(df=df_table_sanit)

        ######################### ENVIA NOTIFICAÇÃO ##################################
        ### PRECISA CONFIGURAR AS CREDENCIAIS PARA ACESSAR O KEYVAUT - SCRIPT NO notification_controller.py
        # envia_notificacao(
        #     destinatario='edvaldo.ferreira@minervafoods.com',
        #     assunto='Notificação de Sanitização de Tabela',
        #     lista_tabelas=['tabela1', 'tabela2', 'tabela3']
        # )

    except Exception as e:
        print(f"Ocorreu um erro no processo: {e}")


if __name__ == "__main__":
    main()
    print("Processo finalizado com sucesso!!!")
