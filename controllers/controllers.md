# 📂 Controllers

Esta pasta contém módulos que gerenciam as diferentes partes do processo de sanitização.

## Módulos

### env_controller.py

Gerencia as variáveis de ambiente necessárias para o projeto.

#### Funções:

- `load_environment_variables()`: Carrega as variáveis de ambiente a partir do arquivo `.env`.

### tables_sanitization_controller.py

Contém funções para listar, criar e excluir tabelas e schemas no banco de dados.

#### Funções:

- `list_table_sanitization(data_base: str) -> pd.DataFrame`: Lista as tabelas a serem sanitizadas.
- `create_schema_dbthanos(schema_name: str) -> None`: Cria um schema no banco de dados `dbthanos`.
- `create_table_dbthanos(old_db: str, new_db: str, schema_name: str, table_name: str) -> None`: Cria uma tabela no banco de dados `dbthanos`.
- `drop_table_origin(database: str, schema_name: str, table_name: str) -> None`: Exclui uma tabela do banco de origem.
- `write_log_sanitization(tab_log: str, ddl_type: str, database_name: str, schema_name: str, table_name: str) -> None`: Grava um log de sanitização na tabela especificada e em um arquivo CSV.

### notification_controller.py

Gerencia o envio de notificações por e-mail sobre o status do processo de sanitização.

#### Funções:

- `send_notification(destinatario: str, assunto: str) -> None`: Envia uma notificação por e-mail.
- `get_secret_from_keyvault(vault_url: str, secret_name: str) -> str`: Recupera um segredo do Azure Key Vault.
