from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs


# Função para lidar com requisições POST
def handle_post_request(request):
    # Obtendo o tamanho do conteúdo da requisição
    content_length = int(request.headers["Content-Length"])

    # Lendo o conteúdo da requisição
    post_data = request.rfile.read(content_length)

    # Decodificando o conteúdo da requisição
    post_data_decoded = post_data.decode("utf-8")

    # Processando o conteúdo da requisição (nesse caso, apenas devolvendo o conteúdo)
    response_content = post_data_decoded

    # Definindo o cabeçalho para o download do arquivo PDF
    request.send_response(200)
    request.send_header("Content-type", "application/pdf")
    request.send_header("Content-Disposition", 'attachment; filename="arquivo.pdf"')
    request.end_headers()

    # Escrevendo o conteúdo do arquivo PDF como resposta
    with open("arquivo.pdf", "rb") as file:
        request.wfile.write(file.read())


# Função para lidar com requisições HTTP
def simple_http_request_handler(request, client_address, server):
    if request.command == "POST":
        handle_post_request(request)


# Função principal para iniciar o servidor
def run(server_class=HTTPServer, handler_class=simple_http_request_handler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor rodando na porta {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
