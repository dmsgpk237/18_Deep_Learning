# services.py: 비즈니스 로직 처리
# API 호출이나 데이터 처리 로직을 담당.

import requests
import io
from PIL import Image

# Hugging Face API 설정
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
token = "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"
headers = {"Authorization": f"Bearer {token}"}

# 이미지 생성 함수
def query_model(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Model error: {response.status_code}")
    
def process_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr