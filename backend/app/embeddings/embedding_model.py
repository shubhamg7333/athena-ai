from sentence_transformers import SentenceTransformer

# Load the embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text: str):
    """
    Convert text into an embedding vector.
    """
    return model.encode(text).tolist()