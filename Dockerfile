# Usar uma imagem base oficial do Python com Debian
FROM python:3.9-slim


# Instalar Nginx
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*


# Definir o diretório de trabalho
WORKDIR /app


# Copiar o aplicativo Python e os arquivos de configuração para o container
COPY app.py /app
COPY requirements.txt /app
COPY start.sh /app
COPY nginx.conf /etc/nginx/nginx.conf


# Dar permissão de execução ao script
RUN chmod +x /app/start.sh


# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt


# Expôr a porta que o Nginx vai ouvir
EXPOSE 80


# Comando para iniciar o script que sobe o Nginx e o aplicativo Python
CMD ["./start.sh"]