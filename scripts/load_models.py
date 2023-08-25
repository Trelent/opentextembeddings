from sentence_transformers import SentenceTransformer

print("Loading models...")

allowed_models = [
    "bge-large-en",
    "bge-base-en",
    "gte-large",
    "gte-base",
]

model_map = {
    "bge-large-en": SentenceTransformer("BAAI/bge-large-en"),
    "bge-base-en": SentenceTransformer("BAAI/bge-base-en"),
    "gte-large": SentenceTransformer("thenlper/gte-large"),
    "gte-base": SentenceTransformer("thenlper/gte-base"),
}

print("Done loading models.")
