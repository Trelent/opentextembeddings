#! /bin/bash

# Build docker image, then run it
depot build --load -t gpteam-embeddings .
docker run -p 8000:8000 gpteam-embeddings