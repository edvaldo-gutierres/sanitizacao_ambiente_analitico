# service

Esta pasta contém serviços que gerenciam a conexão e interações com o banco de dados.

## Arquivos

### database.py

Este arquivo define a classe `DatabaseService`, que é responsável por gerenciar a conexão com o banco de dados e fornecer sessões para realizar operações de leitura e escrita.

#### Classes e Funções:

- `DatabaseService`: Classe para gerenciar a conexão e sessões com o banco de dados.
  - `__init__()`: Inicializa a classe, configura a string de conexão, cria o engine e configura o sessionmaker.
  - `get_session()`: Retorna uma nova sessão do banco de dados.
