# Importa bibliotecas
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Importa função de controle de variaveis
from controllers.env_controller import EnvironmentController

# Carrega as variáveis de ambiente
env_vars = EnvironmentController.load_environment_variables()

# Define os parâmetros de conexão
key_vault_url = env_vars["key_vault_url"]
secret_name = env_vars["secret_name"]
smtp_server = env_vars["smtp_server"]
smtp_port = env_vars["smtp_port"]


#  Função que conecta ao Azure Key Vault
def get_secret_from_keyvault(vault_url: str, secret_name: str) -> str:
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    secret = client.get_secret(secret_name)
    return print(secret.value)


# Função para envio de notificação via -email
def send_notification(destinatario: str, assunto: str) -> None:

    # Recupera a senha do e-mail do Key Vault
    email_password = get_secret_from_keyvault(key_vault_url, secret_name)

    remetente = "svc_notificacoes_engdados@minervafoods.com"

    # Cria a mensagem de e-mail
    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = assunto

    # Cria a lista de valores em formato de string
    mensagem = "Processo de Sanitização das tabelas concluído com sucesso."

    # Adiciona o corpo da mensagem
    mensagem_completa = f"{mensagem}\n\n"
    msg.attach(MIMEText(mensagem_completa, "plain"))

    # Configura o servidor SMTP
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(remetente, email_password)
        server.sendmail(remetente, destinatario, msg.as_string())
        server.quit()
        print("E-mail enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
