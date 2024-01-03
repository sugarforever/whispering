# Whispering

Whispering is the API service for transcription.

## Get Started

1. Clone this repository

    ```shell
    git clone git@github.com:sugarforever/whispering.git
    ```

2. Install `poetry`

    Whispering is using `poetry` to manage python dependencies.

    ```shell
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. Go to the cloned directory `whispering`, initialize a poetry shell, and install the dependencies.

    ```shell
    $ cd whispering

    $ poetry shell

    $ poetry install
    ```

4. Copy `.env.example` to `.env` and set OPENAI_API_KEY

    There are 2 environmental variables referenced by the service:
    - X_API_KEYS

        **X_API_KEYS** is used to protect the API endpoint from anonymous usage. You should always pass it as a HTTP header `X-API-KEY`.

    - OPENAI_API_KEY

        **OPENAI_API_KEY** is used to call the OpenAI transcribe API.

5. Start the service

    ```shell
    poetry run uvicorn main:app
    ```

    The service should be up and running on http://localhost:8000



