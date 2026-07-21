from backend.app.rag.retriever import retrieve
from backend.app.services.gemini import generate_response


def ask_pdf(question: str):
    # Retrieve relevant chunks from ChromaDB
    chunks = retrieve(question)

    print("\n===== RETRIEVED CHUNKS =====")

    for i, chunk in enumerate(chunks, 1):
        print(f"\n--- Chunk {i} ---")
        print(chunk)

    print("\n===== END RETRIEVED CHUNKS =====")

    # Combine retrieved chunks
    context = "\n\n".join(chunks)

    prompt = f"""
You are Athena AI, a document question-answering assistant.

Answer the user's question using ONLY the information in the CONTEXT.

IMPORTANT:
- Use the context even if the exact words in the question are not present.
- Understand the meaning of the context and answer based on it.
- Do not use outside knowledge.
- If the context does not contain enough information to answer the question, say exactly:
"I couldn't find the answer in the uploaded document."

CONTEXT:
{context}

USER QUESTION:
{question}

ANSWER:
"""

    return generate_response(prompt)