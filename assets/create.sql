CREATE TABLE [dw_datamart_rh].[dim_categoria]
(
    sk_dim_categoria BIGINT NOT NULL
  , scd_data_inicio DATETIME NOT NULL
  , scd_data_fim DATETIME NULL
  , scd_ativo BIT NOT NULL
  , cod_categoria VARCHAR NOT NULL
  , desc_categoria VARCHAR NULL,
);