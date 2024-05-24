# models

Esta pasta contém os modelos declarativos SQLAlchemy usados no projeto para mapear tabelas do banco de dados em classes Python.

## Arquivos

### tab_logs.py

Define a estrutura da tabela de logs de sanitização.

#### Classes e Colunas:

- `Tables_Sanitization`: Representa a tabela `tab_log_sanitization` no esquema `data_engineer`.
  - `id`: Identificador único (inteiro, chave primária).
  - `ddl_type`: Tipo de operação DDL (string, não nulo).
  - `database_name`: Nome do banco de dados (string, não nulo).
  - `schema_name`: Nome do esquema (string, não nulo).
  - `table_name`: Nome da tabela (string, não nulo).
  - `row_process_timestamp`: Timestamp do processo de linha (datetime, não nulo, valor padrão `func.now()`).

### tables_sanitization.py

Define a estrutura da tabela de sanitização de tabelas analíticas.

#### Classes e Colunas:

- `Tables_Sanitization`: Representa a tabela `tab_analytical_tables_sanitization` no esquema `data_engineer`.
  - `id`: Identificador único (string, chave primária).
  - `server_name`: Nome do servidor (string, não nulo).
  - `database_name`: Nome do banco de dados (string, não nulo).
  - `schema_name`: Nome do esquema (string, não nulo).
  - `table_name`: Nome da tabela (string, não nulo).
  - `total_row_count`: Contagem total de linhas (inteiro, não nulo).
  - `table_create_date`: Data de criação da tabela (datetime, não nulo).
  - `min_date_report`: Data mínima do relatório (datetime, não nulo).
  - `max_date_report`: Data máxima do relatório (datetime, não nulo).
  - `qty_days`: Quantidade de dias (inteiro, não nulo).
  - `row_ingestion_timestamp`: Timestamp de ingestão da linha (datetime, não nulo).

### __init__.py

Arquivo de inicialização para o pacote `models`. Este arquivo permite que a pasta `models` seja tratada como um pacote Python.
