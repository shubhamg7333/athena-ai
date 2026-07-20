import chromadb
from backend.app.embeddings.embedding_model import get_embedding

# Create a persistent ChromaDB client
client = chromadb.PersistentClient(path="backend/vector_db")

# Create (or get) a collection
collection = client.get_or_create_collection(
    name="athena_documents"
)


def add_chunks(chunks):
    """
    Store chunks and their embeddings in ChromaDB.
    """

    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)

        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[chunk],
        )


def search_chunks(query, top_k=3):
    """
    Search the most relevant chunks.
    """

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )

    return results["documents"][0]