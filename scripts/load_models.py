from sentence_transformers import SentenceTransformer

print("Loading models...")

allowed_models = [
    # "bge-large-en",
    # "bge-base-en",
    # "gte-large",
    # "gte-base",
    "all-MiniLM-L6-v2"
]

model_map = {
    # "bge-large-en": SentenceTransformer("BAAI/bge-large-en", quantize=True),
    # "bge-base-en": SentenceTransformer("BAAI/bge-base-en", quantize=True),
    # "gte-large": SentenceTransformer("thenlper/gte-large", quantize=True),
    # "gte-base": SentenceTransformer("thenlper/gte-base", quantize=True),
    "all-MiniLM-L6-v2": SentenceTransformer("all-MiniLM-L6-v2", quantize=True)
}

print("Done loading models.")
