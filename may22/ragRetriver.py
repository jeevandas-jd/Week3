import chromadb
from langchain_experimental.text_splitter import SemanticChunker

import os
from dotenv import load_dotenv
import uuid
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
load_dotenv()

def CreateChromaDB(documnet:str)->bool:
    try:
        #chunk the document into smaller pieces

        with(open(documnet, "r", encoding="utf-8") as f):
            text = f.read()
            print("Document read successfully.\n document datatype is: ", type(text))
            embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            text_splitter = SemanticChunker(GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
                                            breakpoint_threshold_type="percentile")
            chunk=text_splitter.create_documents([text])
            print("Document chunked successfully.\n document datatype is: ", type(chunk))
            #return chunk
        db_Client=chromadb.PersistentClient(path="vector_db/")
        existing_collections = [col.name for col in db_Client.list_collections()]

        if "faq" in existing_collections:
            db_Client.delete_collection("faq")
        collection = db_Client.create_collection("faq")
        texts=[doc.page_content for doc in chunk]
        embeddings = embedding_model.embed_documents(texts)
        collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=[str(uuid.uuid4()) for _ in range(len(texts))],
        )
        print("Documents added to the collection successfully.")
    except Exception as e:
        print(f"Error reading the document: {e}")
        return None






