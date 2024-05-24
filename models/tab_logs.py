# Importa biblioteca
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
# from sqlalchemy.ext.declarative import declarative_base   # Vai entrar em desuso
from sqlalchemy.orm import declarative_base

# Definir a base para os modelos declarativos
Base = declarative_base()

# Definir uma classe modelo, que herda de 'Base'
class Tables_Sanitization(Base):
    __tablename__ = "tab_log_sanitization"
    __table_args__ = {"schema": "data_engineer"}  # Define o esquema do banco de dados
    id = Column(Integer, primary_key=True)
    ddl_type = Column(String, nullable=False)
    database_name = Column(String, nullable=False)	
    schema_name	= Column(String, nullable=False)
    table_name	= Column(String, nullable=False)
    row_process_timestamp = Column(DateTime, nullable=False, default=func.now())
