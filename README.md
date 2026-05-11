# Sistema Integrado com IA

## 1. Contexto do projeto

Este projeto foi criado como parte de um portfólio de Engenharia de Dados com foco em IA aplicada.

A proposta é construir, em etapas, um sistema integrado simples e evolutivo usando Python, Streamlit e OpenAI API.  
Neste momento, o projeto já possui uma funcionalidade de resumo de textos com IA e uma base pronta para evoluir para chatbot e histórico em banco.

## 2. Ideia principal

A ideia do projeto é ter uma aplicação única com múltiplas funcionalidades de IA, começando com:

- Resumo de textos (funcionando)
- Chatbot (em construção)
- Persistência de histórico em banco (planejado para as próximas etapas)

O objetivo não é apenas "fazer funcionar", mas construir com organização, legibilidade e evolução por fases.

## 3. O que já foi feito até agora

Até o momento, foram concluídos os seguintes pontos:

- Estrutura inicial do repositório
- Configuração de segurança para segredos (`.env` no `.gitignore`)
- Arquivo de exemplo de variável de ambiente (`.env.example`)
- Interface inicial em Streamlit
- Prompt específico para resumidor e prompt base para chatbot
- Cliente OpenAI via Responses API
- Integração entre interface e chamada da IA no fluxo de resumo
- Tratamento básico de erros na interface

### Status funcional atual

- `Resumidor`: implementado
- `Chatbot`: placeholder na interface (próximo passo)
- `Banco de dados`: arquivos preparados, implementação pendente

## 4. Arquitetura atual (versão inicial)

### Fluxo do resumidor

1. Usuário cola um texto na interface Streamlit.
2. O app valida se o texto não está vazio.
3. O app chama a função `gerar_resposta_ia(...)`.
4. A função usa `OPENAI_API_KEY` do `.env`.
5. A OpenAI retorna o resumo.
6. O app exibe o resultado na tela.

### Organização de arquivos

```text
sistema_integrado_ia/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── src/
│   ├── __init__.py
│   ├── ai_client.py
│   ├── prompts.py
│   └── database.py
└── tests/
    └── test_database.py
```

## 5. Tecnologias utilizadas

- Python 3.11+
- Streamlit
- OpenAI Python SDK
- python-dotenv
- pytest

## 6. Como executar localmente

### 6.1 Pré-requisitos

- Python 3.11 ou superior
- Git

### 6.2 Instalação

```powershell
cd F:\sistema_integrado_ia
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 6.3 Configurar variável de ambiente

Crie o arquivo `.env` na raiz do projeto com:

```env
OPENAI_API_KEY=sua_chave_aqui
```

Importante:

- Nunca subir `.env` para o GitHub
- Usar apenas um `.env` na raiz do projeto

### 6.4 Rodar a aplicação

```powershell
python -m streamlit run app.py --server.port 8503
```

Depois, abrir no navegador:

```text
http://localhost:8503
```

## 7. Problemas comuns e solução rápida

### Erro `Connection error`

Possível causa: proxy local incorreto no ambiente.  
Solução (sessão atual):

```powershell
Remove-Item Env:HTTP_PROXY -ErrorAction SilentlyContinue
Remove-Item Env:HTTPS_PROXY -ErrorAction SilentlyContinue
Remove-Item Env:ALL_PROXY -ErrorAction SilentlyContinue
```

### Erro `429 insufficient_quota`

Significa falta de cota/saldo na API.

Verificar:

- Billing: https://platform.openai.com/account/billing/overview
- API Keys: https://platform.openai.com/api-keys

## 8. Commits realizados (Dia 1)

Foram organizados em blocos de trabalho:

1. `chore`: estrutura do projeto e segurança
2. `feat`: prompts e cliente OpenAI
3. `feat`: interface Streamlit integrada ao resumidor

Essa organização melhora a leitura do histórico e facilita apresentação em portfólio.

## 9. Próximos passos

- Implementar chatbot com histórico em `st.session_state`
- Criar camada de persistência em SQLite (`database.py`)
- Registrar interações (entrada e saída da IA)
- Melhorar README com prints e arquitetura da versão 2
- Publicar evolução contínua no GitHub com commits pequenos e claros
