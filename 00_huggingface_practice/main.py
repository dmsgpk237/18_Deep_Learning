from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
import io
from PIL import Image
from fastapi.responses import StreamingResponse

app = FastAPI()

# Hugging Face API 설정
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
token = "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"
headers = {"Authorization": f"Bearer {token}"}

# Pydantic 모델을 사용하여 요청 본문을 정의
class ImageRequest(BaseModel):
    inputs: str

# 이미지 생성 함수
def query_model(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Model error: {response.status_code}")

@app.post("/generate-image/")
async def generate_image(request: ImageRequest):
    input_text = request.inputs  # 입력 텍스트

    try:
        # 모델 호출
        image_bytes = query_model({"inputs": input_text})

        # 이미지 처리
        image = Image.open(io.BytesIO(image_bytes))
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        return StreamingResponse(img_byte_arr, media_type="image/png")

    except Exception as e:
        return {"error": str(e)}
