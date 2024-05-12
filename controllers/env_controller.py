from dotenv import load_dotenv
import os


class EnvironmentController:
    @staticmethod
    def load_environment_variables():
        load_dotenv()
        return {
            "server": os.getenv("SERVER"),
            "database": os.getenv("DATABASE"),
            "username": os.getenv("USER"),
            "password": os.getenv("PASSWORD"),
        }
