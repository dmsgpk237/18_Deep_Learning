from fastapi import FastAPI
from routers.router import router  # routers 폴더 내의 router 모듈 임포트

app = FastAPI()

app.include_router(router)
