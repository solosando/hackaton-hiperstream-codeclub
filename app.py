import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)


def criar_grafo(df):
    G = nx.DiGraph()  # Usamos um grafo direcionado, pois as conexões têm uma direção
    for index, row in df.iterrows():
        origem = row["PastaOrigem"]
        destino = row["PastaDestino"]
        G.add_edge(origem, destino)
        # Verificamos se há uma pasta de backup definida
        if "PastaBackup" in row and pd.notna(row["PastaBackup"]):
            backup = row.iloc[4]
            G.add_edge(origem, backup)  # Adicionamos uma aresta para a pasta de backup

    plt.figure(figsize=(30, 20))
    pos = nx.spring_layout(G)  # Layout para posicionar os nós
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=1000,
        node_color="lightblue",
        font_size=10,
        font_weight="bold",
    )
    plt.title("Fluxo")
    plt.savefig(
        "static/grafo.png", format="png"
    )  # Salvando o arquivo no diretório 'static' para que possa ser acessado via web
    plt.close()
    return "static/grafo.png"


def png_para_pdf(arquivo_png):
    pdf_path = "output.pdf"  # Caminho para o arquivo PDF que será gerado
    c = canvas.Canvas("output.pdf", pagesize=letter)
    c.drawImage(arquivo_png, 100, 600, width=400, height=200)
    c.save()
    return pdf_path


# Rota para a página inicial
@app.route("/")
def index():
    return render_template("index.html")


# Rota para lidar com o upload do arquivo CSV
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "Nenhum arquivo enviado"

    file = request.files["file"]

    if file.filename == "":
        return "Nome do arquivo vazio"

    if file:
        # Salva o arquivo CSV temporariamente
        csv_path = "temp.csv"
        file.save(csv_path)

        # Lê o arquivo CSV usando o pandas
        df = pd.read_csv(csv_path, sep=";")

        # Cria o grafo a partir dos dados do CSV
        png_path = criar_grafo(df)

        # Simula a criação do PDF a partir do PNG
        pdf_path = png_para_pdf(png_path)

        # Remove o arquivo CSV temporário
        os.remove(csv_path)

        return render_template(
            "index.html", png_path=png_path, pdf_path=pdf_path, show_png=True
        )


# Rota para baixar o PDF
@app.route("/download")
def download_file():
    pdf_path = request.args.get("pdf_path")
    if pdf_path:
        return send_file(pdf_path, as_attachment=True)
    else:
        return "Arquivo PDF não encontrado"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
