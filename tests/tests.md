# tests

Esta pasta contém testes para verificar a funcionalidade do projeto.

## Arquivos

### test_database.py

Este arquivo contém testes para verificar a conexão com o banco de dados e a existência de tabelas.

#### Testes:

- `test_database_connection()`: Verifica se a conexão com o banco de dados pode ser estabelecida e fechada corretamente.
- `test_table_exists()`: Verifica se a tabela `tab_analytical_tables_sanitization` existe no banco de dados `dw_hml`.
- `test_qty_days_greater_than_60()`: Verifica se há registros na tabela `tab_analytical_tables_sanitization` onde `qty_days` é maior que 60.
