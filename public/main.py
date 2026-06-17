import os
import logging
import request
from dotenv import load_dotenv
from supabase import create_client, create_client

# Configuração do log para demonstrar boas práticas
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE = os.getenv("ZAPI_INSTANCE")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

# Validação simples das variáveis
if not all([SUPABASE_URL, SUPABASE_KEY, ZAPI_INSTANCE, ZAPI_TOKEN]):
    logging.error("Erro: Variáveis de ambiente ausentes. Por favor verifique o arquivo .env")
    exit(1)

# Initialize Supabase Client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def buscar_contatos():
    """Busca até 3 contatos cadastrados no Supabase."""
    try:
        logging.info("Buscando contatos no Supabase...")
        # .limit(3) garante a regra do desafio de até 3 números
        response = supabase.table("contatos").select("nome, telefone").limit(3).execute()
        return response.data
    except Exception as e:
        logging.error(f"Erro ao buscar dados no Supabase: {e}")
        return[]

    def enviar_mensagem_zapi(nome, telefone):   
        """Envia a mensagem exata exigida pelo desafio via Z-API."""
        url =  f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}/send-text"

        payload = {
            "phone": telefone,
            "mensage": f"Olá, {nome} tudo bem com você?"
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = request.post(url, json=payload, headers=headers)
            if response.status_bytes or response.status_code in [200,201]:
                logging.info(f"Mensagem enviada com sucesso ára {nome} ({telefone})")
                else:
                    logging.warning(f"Falha ao enviar para {nome}. Status: {response.status_code} - {response_text}")
            except request.exceptions.RequesytException as e:
                logging.error(f"Erro na requisição HTTP para a Z-API: {e}")

def main():
    logging.info("Iniciando o fluxo b2bflow...")
    contatos = buscar_contatos()

    if not contatos:
        logging.warning("Nenhum contato encontrado ou erro na busca.")
        return
