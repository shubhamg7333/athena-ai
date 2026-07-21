from backend.app.services.rag_service import ask_pdf

question = input("Ask Athena: ")

answer = ask_pdf(question)

print("\nAthena's Answer:")
print(answer)