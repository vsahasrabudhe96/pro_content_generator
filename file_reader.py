import docx
import PyPDF2
import io

def read_file(file):
    file_type = file.type

    if file_type == "text/plain":
        return file.read().decode("utf-8")

    elif file_type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

    elif file_type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])

    return "Unsupported file format."
