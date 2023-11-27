from pdf_parser import parse_pdf
from embeddings import generate_embeddings 
from vector_database import create_database

text = parse_pdf('Rust Programming.pdf')
docs, embedding_function = generate_embeddings(text)
db = create_database(docs, embedding_function)