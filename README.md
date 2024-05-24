# Projeto Sanitização automática de objetos de ambientes analíticos

O objetivo do projeto é automatizar a sanitização de ambientes analíticos, excluindo objetos não utilizados por mais de 60 dias e armazenando-os temporariamente em um banco dedicado para esse fim.

<!--
## Documentação interna
Para mais detalhes sobre o procedimento de sanitização, consulte a [Documentação Interna](https://wiki.minervafoods.com/xwiki/bin/view/Tecnologia/Procedimento%20Operacional%20Padr%C3%A3o/Engenharia%20de%20Dados/.Constru%C3%A7%C3%A3o/Procedimento%20de%20Sanitiza%C3%A7%C3%A3o/).


# Entidades

As entidades elegíveis ao processo de sanitização estão relacionadas na tabela:
```sql
select * from dw_refined.data_engineer.tab_analytical_tables_sanitization
```

A orquestração dos dados que atualizam a tabela, foi desenvolvida no pentaho (by Mateus Malta) e está localizada na pasta:
`/home/.Oficial/Data Governance/Sanitization Tables`:

![Job Orquestratora Pentaho](assets/image.png)

-->

# 📂 Estrutura de Pasta

A estrutura de pastas foi organizada seguindo princípios de orientação a objetos, conforme preferência do autor.

* **controllers/**: Contém módulos que gerenciam as diferentes partes do processo de sanitização.
  - `env_controller.py`: Gerencia as variáveis de ambiente.
  - `tables_sanitization_controller.py`: Contém funções para listar, criar e excluir tabelas e schemas.
  - `notification_controller.py`: Gerencia o envio de notificações por e-mail.
* **log/**: Diretório para armazenar arquivos de log.
  - `log_sanitization.csv`: Arquivo CSV que contém os logs das tabelas sanitizadas.
* **models/**: Contém os modelos declarativos SQLAlchemy.
  - `tab_logs.py`: Define a estrutura da tabela de logs de sanitização.
  - `tables_sanitization.py`: Define a estrutura da tabela de sanitização de tabelas analíticas.
* **service/**: Contém serviços que gerenciam a conexão e interações com o banco de dados.
  - `database.py`: Define a classe `DatabaseService` para gerenciar a conexão com o banco de dados e fornecer sessões.
* **tests/**: Pasta onde se encontram os testes de qualidade de dados.
  - `test_database.py`: Contém testes para verificar a conexão com o banco de dados e a existência de tabelas.


# 💾 Banco de dados e ORM
A tecnologia de banco de dados utilizada foi o SQL Server, e o ORM utilizado foi o sqlalchemy.


# Instalação

1. 📥 Clone o repositório:
    ```sh
    git clone https://github.com/edvaldo-gutierres/artefatos_pentaho
    ```
2. 📦 Instale as dependências:
    ```bash
    pip install -r requirements.txt
    pre-commit install
    ```
3. 🛠️ Configure as variáveis de ambiente criando um arquivo `.env` na raiz do projeto:
    ```
    SERVER=<endereco-do-servidor>
    DATABASE=<nome-do-banco-de-dados>
    USER=<seu-usuario>
    PASSWORD=<sua-senha>
    ```
4. ▶️ Execute o projeto:
    ```sh
    python app.py
    ```
---
