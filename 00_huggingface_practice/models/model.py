# models.py: 데이터 모델 정의
# Pydantic 모델이나 데이터베이스 모델을 정의하는 파일.

from pydantic import BaseModel

class ImageRequest(BaseModel):
    inputs: str