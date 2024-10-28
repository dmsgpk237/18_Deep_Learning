from fastapi import APIRouter
from services.service import query_model, process_image  # services 폴더 내의 service 모듈 임포트
from models.model import ImageRequest  # models 폴더 내의 model 모듈 임포트
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.post("/generate-image/")
async def generate_image(request: ImageRequest):
    input_text = request.inputs
    try:
        # 모델 호출
        image_bytes = query_model({"inputs": input_text})

        # 이미지 처리
        img_byte_arr = process_image(image_bytes)
        return StreamingResponse(img_byte_arr, media_type="image/png")

    except Exception as e:
        return {"error": str(e)}
