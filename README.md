# Projeto Hackathon - Equipe Code Club

## Sobre o Projeto

Este projeto foi desenvolvido para o desafio proposto da HiperStream do hackathon 2024 da Universidade Presbiteriana MAckenzie. O objetvo é criar uma aplicação que recebe um arquivo CSV e retorna um diagrama em formato PDF que pode ser baixado. 

A solução encontrada pela equipe Code Club foi a criação de um site web, que permite ao usuário enviar o arquivo CSV e receber o diagrama PDF correspondente, que corresponde a uma aplicação standalone em python.

## Apresentação da solução
### Arquitetura da solução
Trata-se de uma aplicação web de arquitetura monolítica, que consiste em um servidor web e uma aplicação. O desenho da arquitetura da solução é representado a seguir:

### Tecnologias utilizadas
- Python
- HTML 
- graphviz
- Docker
- Nginx

### Como funciona
A aplicação web foi desenvolvida em Python. O diagrama foi criado utilizando o pacote graphviz, uma coleção de ferramentas de código aberto para visualização de grafos e redes. O diagrama é então convertido para PDF utilizando o pacote fpdf. O site web foi hospedado em um servidor web Nginx, que é um servidor web HTTP e proxy reverso para servidores web. O site web é executado em um container Docker, que hospeda também a aplicação, permitindo-as serem executadas em qualquer sistema operacional. O site web é acessível através de um endereço IP público, que pode ser acessado por qualquer pessoa com acesso à internet. O seguinte diagrama explicita o funcionamento dela como um todo:
![Organizador gráfico de problema e soluções retrô verde e preto](https://github.com/solosando/hackaton-hiperstream-codeclub/assets/112891254/b6d5e502-fd59-416c-bab7-97a79e9757fc)

Nela o usuário envia um arquivo .csv, a aplicação gera um grafo tal qual este:
![alt text](<grafo.png 21-14-40-250.png>)
Exibe-o na página e disponibiliza o arquivo PDF para download, como o do arquivo [text](output.pdf)

A integração web é toda feita por requisiçöes intermediadas por bibliotecas python. 

## Como Implementar a solução
### Pré-requisitos

- Docker instalado no seu sistema para rodar o container.
- Python 3.9 ou versöes superiores

### Instanciando os containers do servidor web e da aplicação

1. Clone o repositório:
` git clone (https://github.com/solosando/hackaton-hiperstream-codeclub/blob/main/README.md) `

2. Construa o container Docker:
`docker build -t my-app .`

3. Rode o container:
`  docker run --name my-app -p 80:80 -d my-app `

Para usar o aplicativo do seu navegadior, acesse http://localhost:8000 ou http://127.0.0.1:8080

## Sobre a Equipe
Equipe Code Club - HIPER-220 

Construído por:
- Ariel  Oliveira Solosando
- Luccas Auada 
- Roberto Rinco 

## Licença
Este projeto está licenciado sob a licença MIT - consulte o arquivo.
