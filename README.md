# Projeto Sanitização automática de objetos de ambientes analíticos

Esse projeto tem como objetivo automatizar o processo de movimentação de entidades (tabelas) não utilizadas em periodo determinado, para um banco de dados denominado [dbthanos]. Onde a partir de um outro periodo determinado deverá ter sua exclusão definitiva do banco de dados, conforme exposta na documentação de procedimento interno da compania.

## Documentação interna
https://wiki.minervafoods.com/xwiki/bin/view/Tecnologia/Procedimento%20Operacional%20Padr%C3%A3o/Engenharia%20de%20Dados/.Constru%C3%A7%C3%A3o/Procedimento%20de%20Sanitiza%C3%A7%C3%A3o/


# Entidades

As entidades elegíveis ao processo de sanitização estão relacionadas na tabela:
```sql
select * from dw_refined.data_engineer.tab_analytical_tables_sanitization
```

A orquestração dos dados que atualizam a tabela, foi desenvolvida no pentaho (by Mateus Malta) e está localizada na pasta:
`/home/.Oficial/Data Governance/Sanitization Tables`:

![Job Orquestratora Pentaho](assets/image.png)



# Estrutura de Pasta

A estrutura de pastas foi organizada seguindo princípios de orientação a objetos, conforme preferência do autor.

* **controller/**: Pasta onde se encontram todas as funções criadas, referentes à operações de banco de dados.
* **model/**: Pasta onde se encontram as classes de banco de dados criadas, referentes às tabelas do banco.
* **assets/**: Pasta onde se encontram os arquivos estáticos, como imagens, planilhas, etc.
* **service/**: Pasta onde se encontram as funções criadas para conexão ao banco de dados.
* **tests/**: Pasta onde se encontram os testes de qualidade de dados.


# Banco de dados e ORM
A tecnologia de banco de dados utilizada foi o SQL Server, e o ORM utilizado foi o sqlalchemy.


# Ambiente
Para instalar as dependências do projeto, execute o comando
```bash
pip install -r requirements.txt
```