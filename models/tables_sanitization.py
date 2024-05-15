# Importa biblioteca
from sqlalchemy import Column, Integer, String, DateTime

# from sqlalchemy.ext.declarative import declarative_base   # Vai entrar em desuso
from sqlalchemy.orm import declarative_base

# Definir a base para os modelos declarativos
Base = declarative_base()


# Definir uma classe modelo, que herda de 'Base'
class Tables_Sanitization(Base):
    __tablename__ = "tab_analytical_tables_sanitization"
    id = Column(String, primary_key=True)
    server_name = Column(String)
    database_name = Column(String)
    schema_name = Column(String)
    table_name = Column(String)
    total_row_count = Column(Integer)
    table_create_date = Column(DateTime)
    min_date_report = Column(DateTime)
    max_date_report = Column(DateTime)
    qty_days = Column(Integer)
    row_ingestion_timestamp = Column(DateTime)
