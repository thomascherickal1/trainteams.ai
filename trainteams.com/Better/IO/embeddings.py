import spacy
from langchain.embeddings.sentence_tranformers import SentenceTransformerEmbeddings

def generate_embeddings(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    tokens = [token.text for token in doc]
    
    embedding_function = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2') 
    return tokens, embedding_function