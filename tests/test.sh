#! /bin/bash

curl http:/localhost:8000/v1/embeddings \
    -H "Content-Type: application/json" \
    -d '{
        "input": "Sweet, I love better embeddings!",
        "model": "all-MiniLM-L6-v2"
    }'