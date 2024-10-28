from pydantic import BaseModel

class ImageRequest(BaseModel):
    inputs: str
