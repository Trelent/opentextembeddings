from sentence_transformers import SentenceTransformer
from fast_sentence_transformers import FastSentenceTransformer

print("Loading models...")

allowed_models = [
    "bge-large-en",
    "bge-base-en",
    "gte-large",
    "gte-base",
    "all-MiniLM-L6-v2",
]

model_map = {
    "bge-large-en": (
        FastSentenceTransformer("BAAI/bge-large-en", quantize=True),
        SentenceTransformer("BAAI/bge-large-en"),
    ),
    "bge-base-en": (
        FastSentenceTransformer("BAAI/bge-base-en", quantize=True),
        SentenceTransformer("BAAI/bge-base-en"),
    ),
    "gte-large": (
        FastSentenceTransformer("thenlper/gte-large", quantize=True),
        SentenceTransformer("thenlper/gte-large"),
    ),
    "gte-base": (
        FastSentenceTransformer("thenlper/gte-base", quantize=True),
        SentenceTransformer("thenlper/gte-base"),
    ),
    "all-MiniLM-L6-v2": (
        FastSentenceTransformer("all-MiniLM-L6-v2", quantize=True),
        SentenceTransformer("all-MiniLM-L6-v2"),
    ),
}

print("Done loading models.")
