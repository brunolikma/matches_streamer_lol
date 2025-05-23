FROM python:3.10-alpine

# Instala dependências do sistema (útil para o requests + dotenv funcionarem bem)
RUN apk add --no-cache build-base

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependência e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto para o container
COPY . .

# Expõe a variável de ambiente para o Python
ENV PYTHONUNBUFFERED=1

# Comando para rodar o main.py
CMD ["python", "main.py"]
