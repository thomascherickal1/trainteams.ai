import regex as re
from PyPDF2 import PdfReader

def parse_pdf(file_path):
    pdfFile = open(file_path, 'rb')
    reader = PdfReader(pdfFile)

    document = ""

    for pageNum in range(len(reader.pages)):
        page = reader.pages[pageNum].extract_text()
        document += page

    document = document.lower()
    
    # Remove punctuation
    document = re.sub(r'[^\w\s]', '', document)
    
    return document
