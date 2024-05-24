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
    server_name = Column(String, nullable=False)
    database_name = Column(String, nullable=False)
    schema_name = Column(String, nullable=False)
    table_name = Column(String, nullable=False)
    total_row_count = Column(Integer, nullable=False)
    table_create_date = Column(DateTime, nullable=False)
    min_date_report = Column(DateTime, nullable=False)
    max_date_report = Column(DateTime, nullable=False)
    qty_days = Column(Integer, nullable=False)
    row_ingestion_timestamp = Column(DateTime, nullable=False)
