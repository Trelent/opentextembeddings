# Open-source Text Embeddings

We made a free OpenAI-like API so you can instantly use better, open-source text embedding models.

| Model                  | MTEB Score | Dimensions | Seq Length | Cost per 10M tokens |
| ---------------------- | ---------- | ---------- | ---------- | ------------------- |
| bge-large-en           | 63.98%     | 1024       | 512        | $0                  |
| bge-base-en            | 63.36%     | 768        | 512        | $0                  |
| gte-large              | 63.13%     | 1024       | 512        | $0                  |
| gte-base               | 62.39%     | 768        | 512        | $0                  |
| text-embedding-ada-002 | 60.99%     | 1536       | 8192       | $1                  |

### Legend

**Model** is the name of the model to use in the API. If it has a red background, we do not support it.

**MTEB Score** is the Massive Text Embedding Benchmark score. It is the average of the 10 downstream tasks in the Text Embedding Benchmark.

**Dimensions** is the number of dimensions of the embedding vectors. Lower is better, as it is cheaper to store in a vector DB.

**Seq Length** is the maximum number of tokens in a sequence. Typically anything above 256 is enough for most use cases, as most embedding models perform poorly with large chunks of text.

**Cost** is the cost per 10M tokens.

### Limitations

To keep this API free and available to as many people as possible, you may only make 1,000 requests per hour. If this is insufficient for your needs, feel free to self-host on your own infrastructure. We recommend at least 4 CPU cores and 16GB of RAM. A GPU is not required, but will speed up requests.
