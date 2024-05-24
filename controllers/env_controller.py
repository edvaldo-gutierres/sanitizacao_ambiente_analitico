from dotenv import load_dotenv
import os
from pathlib import Path


class EnvironmentController:
    @staticmethod
    def load_environment_variables():
        load_dotenv()
        return {
            "server": os.getenv("SERVER"),
            "database": os.getenv("DATABASE"),
            "username": os.getenv("USER"),
            "password": os.getenv("PASSWORD"),
            "key_vault_url": os.getenv("KEY_VAULT_URL"),
            "secret_name": os.getenv("SECRET_NAME"),
            "smtp_server": os.getenv("SMTP_SERVER"),
            "smtp_port": os.getenv("SMTP_PORT"),
        }
