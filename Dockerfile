# Use a imagem base desejada, por exemplo, Python para executar uma aplicação Flask
FROM python:3.9-slim

# Instale o servidor web, por exemplo, Nginx
RUN apt-get update && apt-get install -y nginx

# Copie a configuração do servidor Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copie os arquivos da aplicação
COPY . /app

# Instale as dependências da aplicação, se necessário
WORKDIR /app
RUN pip install -r requirements.txt

# Exponha a porta do servidor web
EXPOSE 80

# Comando para iniciar o servidor Nginx e a aplicação Python
CMD service nginx start && python app.py