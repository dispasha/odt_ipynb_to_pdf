from nbconvert import HTMLExporter
import nbformat
import os
import pdfkit
import json


from html_handler import merge_htmls

def convert(name1, name2):
    with open("config.json") as f:
        liboffice = json.load(f)["libre_office_path"]
    cwd=os.getcwd()
    print("Converting document...")
    name1=name1.replace('/', '\\')
    p = os.popen(fR'"{liboffice}" --convert-to html --outdir {cwd}\temp "{name1}"').read()

    print("Converting notebook...")

    name1 = name1[name1.rfind('\\')+1:].replace('odt', 'html')
    config = {
      'Exporter': {
          'template_paths': ['templates'],
      },
    }
    html_exporter = HTMLExporter(config)
    html_exporter.exclude_input=True
    html_exporter.exclude_input_prompt=True
    html_exporter.exclude_output_prompt=True
    with open(name2, encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    body_output = html_exporter.from_notebook_node(nb)[0]
    html_exporter.exclude_input=False
    html_exporter.exclude_output=True
    body_input = html_exporter.from_notebook_node(nb)[0]
    with open(F'temp/{name1}', 'r', encoding="windows-1251", errors="ignore") as test:
        word_html = test.read()
    merge_htmls(body_input, body_output, word_html)
    pdfkit.from_file("temp/temp.html", "out.pdf", options={"enable-local-file-access": None})
    print("ok")
