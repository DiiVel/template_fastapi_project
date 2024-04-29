FROM python:3.11-alpine

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN python -m pip install --no-cache-dir poetry==1.7.1 \
    && poetry config virtualenvs.create false \
    && poetry install --without dev --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}

COPY . /app

EXPOSE 8000

ENTRYPOINT [ "/app/entrypoint.sh" ]