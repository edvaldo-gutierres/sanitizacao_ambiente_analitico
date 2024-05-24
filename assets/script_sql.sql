USE dw_hml;

/*
DROP TABLE IF EXISTS dw_hml.data_engineer.tab_log_sanitization ;
*/
SELECT * FROM dw_hml.data_engineer.tab_log_sanitization (NOLOCK)

-- Tabela de controle
SELECT id,
       server_name,
       database_name,
       schema_name,
       table_name,
       total_row_count,
       table_create_date,
       min_date_report,
       max_date_report,
       qty_days,
       row_ingestion_timestamp
FROM dw_hml.data_engineer.tab_analytical_tables_sanitization
WHERE 1 = 1
      AND qty_days > 60;



-- tabelas exemplos
SELECT * FROM dw_hml.datamart_rh.dim_calendario;
SELECT * FROM dw_hml.datamart_rh.dim_categoria;
SELECT * FROM dw_hml.datamart_rh.dim_empresa;
SELECT * FROM dw_hml.datamart_rh.dim_evento;
SELECT * FROM dw_hml.datamart_rh.dim_filial;
SELECT * FROM dw_hml.datamart_rh.dim_funcao;
SELECT * FROM dw_hml.datamart_rh.dim_relacao_emprego;
SELECT * FROM dw_hml.datamart_rh.dim_secao;
SELECT * FROM dw_hml.datamart_rh.dim_sindicato;
SELECT * FROM dw_hml.datamart_rh.dim_situacao;
SELECT * FROM dw_hml.datamart_rh.dim_tipo_admissao;
SELECT * FROM dw_hml.datamart_rh.dim_tipo_funcionario;
SELECT * FROM dw_hml.datamart_rh.dim_tipo_situacao;
SELECT * FROM dw_hml.datamart_rh.fato_funcionario_evento;
SELECT * FROM dw_hml.datamart_rh.tab_rh_br_justificativas_fluig;
SELECT * FROM dw_hml.datamart_rh.tab_rh_br_justificativas_infracao;
SELECT * FROM dw_hml.datamart_rh.tab_rh_br_stage_KSB1_custo_medio;
SELECT * FROM dw_hml.datamart_rh.tab_rh_wip_movimentacoes;


-- TABELAS DE EXEMPLO NO DBTHANOS
SELECT * FROM dbthanos.dw_hml_datamart_rh.dim_calendario;
SELECT * FROM dbthanos.dw_hml_datamart_rh.dim_categoria;
SELECT * FROM dbthanos.dw_hml_datamart_rh.dim_empresa;
SELECT * FROM dbthanos.dw_hml_datamart_rh.dim_evento;
SELECT * FROM dbthanos.dw_hml_datamart_rh.dim_filial;
SELECT * FROM dbthanos.dw_hml_datamart_rh.dim_funcao;
SELECT * FROM dbthanos.dw_hml_datamart_rh.dim_relacao_emprego;
SELECT * FROM dbthanos.dw_hml_datamart_rh.dim_secao;
SELECT * FROM dbthanos.dw_hml_datamart_rh.dim_sindicato;
SELECT * FROM dbthanos.dw_hml_datamart_rh.dim_situacao;
SELECT * FROM dbthanos.dw_hml_datamart_rh.dim_tipo_admissao;
SELECT * FROM dbthanos.dw_hml_datamart_rh.dim_tipo_funcionario;
SELECT * FROM dbthanos.dw_hml_datamart_rh.dim_tipo_situacao;
SELECT * FROM dbthanos.dw_hml_datamart_rh.fato_funcionario_evento;
SELECT * FROM dbthanos.dw_hml_datamart_rh.pentaho_log_job;
SELECT * FROM dbthanos.dw_hml_datamart_rh.tab_rh_br_justificativas_fluig;
SELECT * FROM dbthanos.dw_hml_datamart_rh.tab_rh_br_justificativas_infracao;
SELECT * FROM dbthanos.dw_hml_datamart_rh.tab_rh_br_stage_KSB1_custo_medio;
SELECT * FROM dbthanos.dw_hml_datamart_rh.tab_rh_wip_movimentacoes;


-- EXCLUI TABELAS DE EXEMPLO DO DBTHANOS

DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.dim_calendario;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.dim_categoria;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.dim_empresa;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.dim_evento;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.dim_filial;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.dim_funcao;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.dim_relacao_emprego;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.dim_secao;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.dim_sindicato;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.dim_situacao;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.dim_tipo_admissao;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.dim_tipo_funcionario;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.dim_tipo_situacao;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.fato_funcionario_evento;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.tab_rh_br_justificativas_fluig;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.tab_rh_br_justificativas_infracao;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.tab_rh_br_stage_KSB1_custo_medio;
DROP TABLE IF EXISTS dbthanos.dw_hml_datamart_rh.tab_rh_wip_movimentacoes;


-- Copiando tabelas de exemplo do banco de dados dw para o banco de dados dw_hml


SELECT * 
INTO dw_hml.datamart_rh.dim_calendario
FROM dw.datamart_rh.dim_calendario;

SELECT * 
INTO dw_hml.datamart_rh.dim_categoria
FROM dw.datamart_rh.dim_categoria;

SELECT * 
INTO dw_hml.datamart_rh.dim_empresa
FROM dw.datamart_rh.dim_empresa;

SELECT * 
INTO dw_hml.datamart_rh.dim_evento
FROM dw.datamart_rh.dim_evento;

SELECT * 
INTO dw_hml.datamart_rh.dim_filial
FROM dw.datamart_rh.dim_filial;

SELECT * 
INTO dw_hml.datamart_rh.dim_funcao
FROM dw.datamart_rh.dim_funcao;

SELECT * 
INTO dw_hml.datamart_rh.dim_relacao_emprego
FROM dw.datamart_rh.dim_relacao_emprego;

SELECT * 
INTO dw_hml.datamart_rh.dim_secao
FROM dw.datamart_rh.dim_secao;

SELECT * 
INTO dw_hml.datamart_rh.dim_sindicato
FROM dw.datamart_rh.dim_sindicato;

SELECT * 
INTO dw_hml.datamart_rh.dim_situacao
FROM dw.datamart_rh.dim_situacao;

SELECT * 
INTO dw_hml.datamart_rh.dim_tipo_admissao
FROM dw.datamart_rh.dim_tipo_admissao;

SELECT * 
INTO dw_hml.datamart_rh.dim_tipo_funcionario
FROM dw.datamart_rh.dim_tipo_funcionario;

SELECT * 
INTO dw_hml.datamart_rh.dim_tipo_situacao
FROM dw.datamart_rh.dim_tipo_situacao;

SELECT * 
INTO dw_hml.datamart_rh.fato_funcionario_evento
FROM dw.datamart_rh.fato_funcionario_evento;

SELECT * 
INTO dw_hml.datamart_rh.tab_rh_br_justificativas_fluig
FROM dw.datamart_rh.tab_rh_br_justificativas_fluig;

SELECT * 
INTO dw_hml.datamart_rh.tab_rh_br_justificativas_infracao
FROM dw.datamart_rh.tab_rh_br_justificativas_infracao;

SELECT * 
INTO dw_hml.datamart_rh.tab_rh_br_stage_KSB1_custo_medio
FROM dw.datamart_rh.tab_rh_br_stage_KSB1_custo_medio;

SELECT * 
INTO dw_hml.datamart_rh.tab_rh_wip_movimentacoes
FROM dw.datamart_rh.tab_rh_wip_movimentacoes;





