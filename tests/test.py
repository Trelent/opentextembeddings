import openai

openai.api_base = "http://localhost:8000/v1"
embed = openai.Embedding.create(
    model="all-MiniLM-L6-v2", input="Hey, is this API working?"
)
print(embed)
