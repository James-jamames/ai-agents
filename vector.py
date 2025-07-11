import os
import pandas as pd

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

df = pd.read_csv('realistic_restaurant_reviews.csv')

embedding_function = OllamaEmbeddings(model="mxbai-embed-large")

persist_directory = "./chroma_langchain_db"

already_exists = os.path.exists(persist_directory)

if not already_exists:
    ids = []
    documents = []
    
    for i, row in df.iterrows():
        document = Document(
            id=str(i),
            page_content=row['title'] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]}
        )

        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=persist_directory,
    embedding_function=embedding_function
)

if not already_exists:
    vector_store.add_documents(documents=documents, ids=ids)