from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Header, Request, HTTPException, Depends, Security, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from pathlib import Path

from sqlalchemy.orm import Session
import openai
from auth import get_api_key
from logger import get_logger
from schemas import TranscribeRequest
from services import WhisperService, LLMService


logger = get_logger(__name__)

servers = [
    {"url": "http://localhost:8000", "description": "Whispering"}
]

app = FastAPI(servers=servers)

origins = [ "*" ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def serve_readme(request: Request):
    index_path = Path("web/index.html")
    if index_path.is_file():
        with open(index_path, "r", encoding="utf-8") as html_file:
            return html_file.read()
    else:
        raise HTTPException(status_code=404, detail="NOT FOUND")


@app.post("/v1/transcribe")
def transcribe(file: UploadFile, api_key: str = Security(get_api_key)):
    logger.debug(f"Transcribing {file}")

    transcription = None
    summary = None
    with open(file.filename, 'wb') as f:
        while contents := file.file.read(1024 * 1024):
            f.write(contents)

        transcription = WhisperService.transcribe(file.filename)
        summary = LLMService.summarize(transcription)

    return {
        "transcription": transcription,
        "summary": summary
    }