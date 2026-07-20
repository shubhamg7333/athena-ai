from app.embeddings.embedding_model import get_embedding

vector = get_embedding("Hello Athena AI!")

print(type(vector))
print(len(vector))
print(vector[:10])