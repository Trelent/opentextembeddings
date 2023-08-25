from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from .model import (
    Embedding,
    EmbeddingException,
    EmbeddingRequest,
    EmbeddingResponse,
    Usage,
)
from .embed import allowed_models, get_text_embedding, get_tokenized_inputs

app = FastAPI()
version = "0.0.1"


@app.exception_handler(EmbeddingException)
async def exception_handler(request: Request, exc: EmbeddingException):
    return JSONResponse(status_code=exc.code, content=exc.json())


@app.get("/")
@app.get("/v1")
async def main_route():
    return {"version": version}


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
    total_tokens = get_tokenized_inputs(model, input)

    # TODO: We could auto-chunk inputs into 512-token chunks here, but maybe this is just an extra option for future?

    # Get the embeddings for each input and build our response
    embeddings = get_text_embedding(model, input)
    embedding_list = [
        Embedding(object="embedding", embedding=embedding, index=index)
        for index, embedding in enumerate(embeddings)
    ]
    print(embedding_list)

    return EmbeddingResponse(
        object="list",
        data=embedding_list,
        model=model,
        usage=Usage(prompt_tokens=total_tokens, total_tokens=total_tokens),
    )
