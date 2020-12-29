import os
import docx


def read_docx(docx_file):
    return docx.Document(docx_file)


def docx_to_txt(docx_file):
    doc_file = read_docx(docx_file)
    output_file = os.path.splitext(docx_file)[0] + ".txt"

    with open(output_file, "w") as file_:
        for paragraph in doc_file.paragraphs:
            file_.write(paragraph.text + "\n")

    return output_file


def read_txt(txt_file):
    with open(txt_file, "r") as f:
        text = f.read()

    return text


def get_text(uploaded_file):
    file_ext = os.path.splitext(uploaded_file)[1]

    print("Reading document...")
    if file_ext == ".docx":
        txt_file = docx_to_txt(uploaded_file)
        text = read_txt(txt_file)

    if file_ext == ".txt":
        text = read_txt(uploaded_file)

    return text
