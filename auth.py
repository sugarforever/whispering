from fastapi import FastAPI, HTTPException, Security, status
from fastapi.security import APIKeyHeader
import os

api_keys = os.environ["X_API_KEYS"]

API_KEYS = api_keys.split(",")

api_key_header = APIKeyHeader(name="X-API-Key")


def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
    if api_key_header in API_KEYS:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )
