from sentence_transformers import SentenceTransformer

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


def get_text_embedding(model_name: str, input: list[str]):
    model = model_map[model_name]
    embeddings = model.encode(input)
    return embeddings.tolist()


def get_tokenized_inputs(model_name: str, input: list[str]):
    model = model_map[model_name]
    tokens_count = 0
    for i in input:
        tokenized_input = model.tokenize(i)
        print(tokenized_input)

        tokens_count += len(tokenized_input["input_ids"].tolist())
    return tokens_count
