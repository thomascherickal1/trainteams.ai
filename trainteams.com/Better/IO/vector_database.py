from langchain.vectorstores import DeepLake

def create_database(docs, embedding_function):
    db = DeepLake.from_texts(docs, embedding_function, dataset_path="./deeplake_db")
    return db