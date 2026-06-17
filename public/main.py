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

