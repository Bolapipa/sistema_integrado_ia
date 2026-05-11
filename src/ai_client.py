# Carrega variáveis de ambiente do arquivo .env
from dotenv import load_dotenv

# Biblioteca oficial da OpenAI
from openai import OpenAI

# Biblioteca para acessar variáveis de ambiente
import os

import httpx

# Garante que o .env seja carregado
load_dotenv()


def gerar_resposta_ia(
    texto_usuario: str,
    prompt_sistema: str,
    modelo: str = "gpt-5.4-mini"
) -> str:
    """
    Gera resposta da IA com a Responses API.

    Parâmetros:
    - texto_usuario: texto enviado pelo usuário
    - prompt_sistema: instrução de comportamento da IA
    - modelo: modelo que será utilizado
    """

    # Busca chave no ambiente
    api_key = os.getenv("OPENAI_API_KEY")

    # Validação para evitar chamada sem chave
    if not api_key:
        raise ValueError("OPENAI_API_KEY não encontrada no arquivo .env")

    # Cria cliente autenticado
    client = OpenAI(
    api_key=api_key,
    http_client=httpx.Client(trust_env=False)
)

    # Chama a Responses API
    resposta = client.responses.create(
        model=modelo,
        input=[
            {
                "role": "system",
                "content": [
                    {"type": "input_text", "text": prompt_sistema}
                ],
            },
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": texto_usuario}
                ],
            },
        ],
    )

    # Retorna apenas o texto final da resposta
    return resposta.output_text.strip()
