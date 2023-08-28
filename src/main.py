import time
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
import os
import redis

from .db import test_connection, track_total_tokens
from .embed import allowed_models, get_text_embedding, get_tokenized_inputs
from .limit import RedisRateLimiter
from .model import (
    Embedding,
    EmbeddingException,
    EmbeddingRequest,
    EmbeddingResponse,
    Usage,
)

load_dotenv()
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_USER = os.getenv("REDIS_USER")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_INSTANCE = redis.Redis(
    host=REDIS_HOST,
    username=REDIS_USER,
    password=REDIS_PASSWORD,
    port=REDIS_PORT,
    ssl=True,
)
VERSION = "0.0.1"

if not test_connection(REDIS_INSTANCE):
    raise Exception("Redis connection failed.")
else:
    print("Redis connection successful.")

app = FastAPI()
# app.add_middleware(
#    RedisRateLimiter, max_requests=100, time_window=3600, redis_instance=REDIS_INSTANCE
# )


@app.exception_handler(EmbeddingException)
async def exception_handler(request: Request, exc: EmbeddingException):
    return JSONResponse(status_code=exc.code, content=exc.json())


@app.get("/")
@app.get("/v1")
async def main_route():
    # return {"version": VERSION}
    # Return empty html page to prevent 404
    return Response(
        content="""
                    <html>
                        <head>
                            <meta name="loadforge-site-verification" content="90d744ffc2b8a6e92c67b11d3a445ac63353ed2c055ef97b9b1b4a1751aeb2fdc8c833b1708fc834c8c6db26adad6601bf34b31532300db9421b4cd0b4330a9f" />
                        </head>
                        <body>
                            <h1>Version: """
        + VERSION
        + """</h1>
                        </body>
                    </html>
                    """,
        media_type="text/html",
    )


@app.post("/v1/embeddings")
async def embeddings(request: EmbeddingRequest) -> EmbeddingResponse:
    model = request.model
    input = request.input
    # user = request.user

    if model not in allowed_models:
        exception = EmbeddingException(
            f"Model {model} not found.", "invalid_request_error", "model", 400
        )
        raise exception

    # If input is a str, convert to list
    input = input if isinstance(input, list) else [input]

    # Get the token count for each input
    tokenize_start = time.time()
    total_tokens = get_tokenized_inputs(model, input)
    track_total_tokens(REDIS_INSTANCE, total_tokens)
    tokenize_end = time.time()

    # TODO: We could auto-chunk inputs into 512-token chunks here, but maybe this is just an extra option for future?

    # Get the embeddings for each input and build our response
    embedding_start = time.time()
    embeddings = get_text_embedding(model, input)
    embedding_list = [
        Embedding(object="embedding", embedding=embedding, index=index)
        for index, embedding in enumerate(embeddings)
    ]
    embedding_end = time.time()

    print(f"Tokenize time: {tokenize_end - tokenize_start}")
    print(f"Embedding time: {embedding_end - embedding_start}")

    return EmbeddingResponse(
        object="list",
        data=embedding_list,
        model=model,
        usage=Usage(prompt_tokens=total_tokens, total_tokens=total_tokens),
    )
