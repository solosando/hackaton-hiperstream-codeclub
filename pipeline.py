import requests
import csv
import graphviz
import io
import base64
from fpdf import FPDF


def read_file_from_website(url: str) -> str:
    response = requests.get(url)
    return response.text


def transform_csv_to_flowchart(csv_content: str) -> graphviz.Digraph:
    flowchart = graphviz.Digraph()

    # Parse the CSV content and add nodes and edges to the flowchart
    reader = csv.reader(csv_content.splitlines())
    for row in reader:
        flowchart.node(row[0], row[0])
        if len(row) > 1:
            flowchart.edge(row[0], row[1])

    return flowchart


def generate_pdf(flowchart: graphviz.Digraph) -> bytes:
    # Render the flowchart as a PDF
    pdf = flowchart.pipe(format="pdf")

    return pdf


def send_pdf_to_webpage(pdf_content: bytes, url: str) -> None:

    # Send the PDF content back to the webpage using a POST request
    files = {"file": ("flowchart.pdf", pdf_content, "application/pdf")}
    requests.post(url, files=files)


if __name__ == "__main__":
    # Read the CSV file from the website
    csv_content = read_file_from_website("http://localhost/file.csv")

    # Transform the CSV content into a flowchart
    flowchart = transform_csv_to_flowchart(csv_content)

    # Generate a PDF of the flowchart
    pdf_content = generate_pdf(flowchart)

    # Send the PDF content back to the webpage
    send_pdf_to_webpage(pdf_content, "http://localhost/")
