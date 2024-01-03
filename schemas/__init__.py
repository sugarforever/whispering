from fastapi import UploadFile
from pydantic import BaseModel, Field

class TranscribeRequest(BaseModel): 
    file: UploadFile