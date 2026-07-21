from backend.app.rag.retriever import retrieve

results = retrieve("What is Design Thinking?")

print("\nRetrieved Chunks:\n")

for i, chunk in enumerate(results, start=1):
    print(f"Chunk {i}")
    print(chunk)
    print("-" * 50)