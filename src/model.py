from typing import Optional
from pydantic import BaseModel


class Embedding(BaseModel):
    object: str
    embedding: list[float]
    index: int


class Usage(BaseModel):
    prompt_tokens: int
    total_tokens: int


class EmbeddingRequest(BaseModel):
    model: str
    input: str | list[str]


class EmbeddingResponse(BaseModel):
    object: str
    data: list[Embedding]
    model: str
    usage: Usage


class EmbeddingException(Exception):
    def __init__(
        self,
        message: str,
        error_type: Optional[str] = None,
        param: Optional[str] = None,
        code: Optional[int] = None,
    ):
        super().__init__(message)
        self.message = message
        self.error_type = error_type
        self.param = param
        self.code = code

    def json(self):
        return {
            "error": {
                "message": self.message,
                "type": self.error_type,
                "param": self.param,
                "code": self.code,
            }
        }
