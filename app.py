import csv
import graphviz
import io
from fpdf import FPDF
import requests


def read_file_from_website(url: str) -> str:
    """
    Recebendo o arquivo da página web
    """
    response = requests.get(url)
    return response.text


def transform_csv_to_flowchart(csv_content: str) -> graphviz.Digraph:
    """
    Transformando o arquivo csv em um grafo
    """
    flowchart = graphviz.Digraph()
    reader = csv.reader(csv_content.splitlines())
    for row in reader:
        flowchart.node(row[0], row[0])
        if len(row) > 1:
            flowchart.edge(row[0], row[1])
    return flowchart


def generate_pdf(flowchart: graphviz.Digraph) -> bytes:
    """
    Transformando o grafo em um pdf
    """
    pdf = flowchart.pipe(format="pdf")
    return pdf


def send_pdf_to_webpage(pdf_content: bytes, url: str) -> None:
    """
    Mandando o pdf para a página usando um POST request
    """
    files = {"file": ("flowchart.pdf", pdf_content, "application/pdf")}
    requests.post(url, files=files)


def create_flowchart_from_csv_url(csv_url: str, webpage_url: str) -> None:
    """
    Função integrando o processo
    """
    csv_content = read_file_from_website(csv_url)
    flowchart = transform_csv_to_flowchart(csv_content)
    pdf_content = generate_pdf(flowchart)
    send_pdf_to_webpage(pdf_content, webpage_url)


if __name__ == "__main__":
    csv_url = "http://localhost/file.csv"
    webpage_url = "http://localhost/"
    create_flowchart_from_csv_url(csv_url, webpage_url)
