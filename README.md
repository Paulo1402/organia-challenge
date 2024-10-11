# ❤️ OrganIA Challenge

## 🖥️ Instalação
### Dependências
* Python 3.10 - https://www.python.org/downloads/
* Docker - https://docs.docker.com/get-started/get-docker/

Nesse projeto foi utilizado o gerenciador de projeto `uv`, porém pode ser instalado usando qualquer gerenciador que
entenda o arquivo `requirements.txt` ou o arquivo `pyproject.toml` para instalar as dependências.

Para seguir a instalação utilizando o `uv` basta possuir qualquer versão do Python 3 instalada e 
executar os seguintes comandos:

```bash
pip install uv # Instala o uv globalmente

uv python install 3.10 # Caso não tenha o python 3.10 instalado
uv sync # Instala as dependências do projeto
```

### Configuração

Na raíz do projeto, crie um arquivo chamado `.env` com as seguintes variáveis de ambiente:
```
ENVIRONMENT=development
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=organia-challenge
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

## ▶️ Execução
Para rodar o projeto primeiro é necessário subir o banco de dados, para isso execute o seguinte comando:
```bash
docker-compose up -d
```

Após o banco de dados estar rodando, execute o seguinte comando para rodar o projeto:
```bash
fastapi dev
```

O projeto estará rodando em `http://localhost:8000`.


## 📔 Documentação
A documentação da API pode ser acessada em `http://localhost:8000/docs`.

## 🧪 Testes
Para rodar os testes execute o seguinte comando:
```bash
uv run pytest
```

## 🛠 Tecnologias
- Python
- FastAPI
- Pydentic
- Peewee
- Docker
- PostgreSQL
