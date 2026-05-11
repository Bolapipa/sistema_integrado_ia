# Importa o Streamlit para criar a interface web
import streamlit as st

# Importa a função que chama a OpenAI
from src.ai_client import gerar_resposta_ia

# Importa o prompt específico do resumidor
from src.prompts import RESUMO_PROMPT

# Título principal da aplicação
st.title("Sistema Integrado com IA")

# Texto introdutório
st.write("Primeira versão do meu projeto com Streamlit.")

# Menu lateral para escolher funcionalidade
opcao = st.sidebar.selectbox(
    "Escolha uma funcionalidade:",
    ["Resumidor", "Chatbot"]
)

# Bloco da funcionalidade de resumo
if opcao == "Resumidor":
    # Cabeçalho da seção
    st.header("Resumidor de Textos")

    # Campo para o usuário colar o texto
    texto = st.text_area("Cole aqui o texto que você quer resumir:")

    # Botão para gerar o resumo
    if st.button("Gerar resumo"):
        # Validação para evitar chamada com texto vazio
        if texto.strip() == "":
            st.warning("Digite um texto antes de gerar o resumo.")
        else:
            try:
                # Chama a OpenAI usando a função do ai_client
                resumo = gerar_resposta_ia(
                    texto_usuario=texto,
                    prompt_sistema=RESUMO_PROMPT,
                    modelo="gpt-5.4-mini"
                )

                # Exibe o resultado da IA
                st.subheader("Resumo gerado:")
                st.write(resumo)

            except Exception as erro:
                # Mostra erro amigável caso algo falhe
                st.error(f"Erro ao gerar resumo: {erro}")

# Bloco da funcionalidade de chatbot (ainda em construção)
if opcao == "Chatbot":
    # Cabeçalho da seção
    st.header("Chatbot")
    st.write("Próximo passo: conectar o chatbot com IA e histórico.")
