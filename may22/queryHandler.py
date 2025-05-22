from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
import chromadb

def get_chroma_collection(path="vector_db/", collection_name="faq"):
    chroma_client = chromadb.PersistentClient(path=path)
    return chroma_client.get_collection(name=collection_name)


def get_query_embedding(query, model_name="models/embedding-001"):
    embedding_model = GoogleGenerativeAIEmbeddings(model=model_name)
    return embedding_model.embed_query(query)



def search_collection(collection, embedding, n_results=2):
    result = collection.query(query_embeddings=[embedding], n_results=n_results)
    documents = result["documents"][0] if result and result["documents"] else []
    return documents



def generate_answer(context_docs, user_query, model_name="gemini-2.0-flash"):
    if context_docs is None:
        print("Context not fetched from the documnet")
        return
    context = "\n".join(context_docs)
    #print(f"context_docs :\n\t{context_docs}")
    prompt = f"""Use the following context to answer the user's question:

    Context:
    {context}

    Question:
    {user_query}
    """
    chat_model = ChatGoogleGenerativeAI(model=model_name, temperature=0.2)
    response = chat_model([HumanMessage(content=prompt)])
    return response.content
