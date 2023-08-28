from fast_sentence_transformers import FastSentenceTransformer
from sentence_transformers import SentenceTransformer

allowed_models = [
    # "bge-large-en",
    "bge-base-en",
    # "gte-large",
    "gte-base",
    "all-MiniLM-L6-v2",
]

model_map = {
    # "bge-large-en": (FastSentenceTransformer("BAAI/bge-large-en", quantize=True), SentenceTransformer("BAAI/bge-large-en")),
    "bge-base-en": (
        FastSentenceTransformer("BAAI/bge-base-en", quantize=True),
        SentenceTransformer("BAAI/bge-base-en"),
    ),
    # "gte-large": (FastSentenceTransformer("thenlper/gte-large", quantize=True), SentenceTransformer("thenlper/gte-large")),
    "gte-base": (
        FastSentenceTransformer("thenlper/gte-base", quantize=True),
        SentenceTransformer("thenlper/gte-base"),
    ),
    "all-MiniLM-L6-v2": (
        FastSentenceTransformer("all-MiniLM-L6-v2", quantize=True),
        SentenceTransformer("all-MiniLM-L6-v2"),
    ),
}


def get_text_embedding(model_name: str, input: list[str]):
    fast_model = model_map[model_name][0]
    embeddings = fast_model.encode(input)
    return embeddings.tolist()


def get_tokenized_inputs(model_name: str, input: list[str]):
    tokenize_model = model_map[model_name][1]
    tokens_count = 0
    for i in input:
        tokenized_input = tokenize_model.tokenize(i)
        tokens_count += len(tokenized_input["input_ids"].tolist())
    return tokens_count
