FROM python:3.11
LABEL Name=gpteam-embeddings
LABEL Version=0.0.1
LABEL maintainer="Trelent Inc."

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Install sentence-transformers
RUN pip install sentence-transformers poetry

# Load the models
COPY ./scripts/load_models.py /app/scripts/load_models.py
RUN python /app/scripts/load_models.py

# Install deps
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the source code
COPY ./src ./src
WORKDIR /app

# Run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0"]