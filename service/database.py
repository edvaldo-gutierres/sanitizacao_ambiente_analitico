from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.tab_logs import Base

# Importa função de controle de variaveis
from controllers.env_controller import EnvironmentController

# Carrega as variáveis de ambiente
env_vars = EnvironmentController.load_environment_variables()

# Define os parâmetros de conexão
server = env_vars["server"]
database = env_vars["database"]
username = env_vars["username"]
password = env_vars["password"]


class DatabaseService:
    """Classe para gerenciar a conexão e sessões com o banco de dados."""

    def __init__(self):
        """
        Inicializa a classe DatabaseService.
        - Monta a string de conexão usando as variáveis de ambiente.
        - Cria o engine que gerencia a conexão com o banco de dados.
        - Cria um gerenciador de sessões (Session) vinculado ao engine.
        """
        # Define a string de conexão para o banco de dados usando o driver ODBC para SQL Server
        connection_string = (
            f"mssql+pyodbc://{username}:{password}@{server}/{database}"
            f"?driver=ODBC+Driver+17+for+SQL+Server"
        )

        # Cria um objeto Engine que faz a ponte entre o banco de dados e a aplicação
        self.engine = create_engine(connection_string)

        # Cria as tabelas no banco de dados
        Base.metadata.create_all(self.engine)                        

        # Configura o factory sessionmaker para criar novas sessões vinculadas ao engine
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        """
        Retorna uma nova sessão do banco de dados.
        - As sessões são usadas para realizar operações de leitura e escrita no banco de dados.
        """
        return self.Session()
