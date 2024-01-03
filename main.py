from fastapi import FastAPI

app = FastAPI()          # FastAPI() : class
from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from routes.homes import router as event_router
from routes.gadgets import router as event_router1
from routes.positionings import router as event_router2
app.include_router(event_router, prefix='/home')
app.include_router(event_router1, prefix='/gadgets')
app.include_router(event_router2, prefix='/positionings')

from fastapi import Request
from fastapi.templating import Jinja2Templates

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")      # JInja class 실행시키기

@app.get("/")
async def root(request:Request):   # 콜론 뒤 타입 입력해줌(이 타입은 Request다)
    # return {"message": "Youjin World!"}
    # root() 호출 -> http://192.168.10.184:8000/
    # html 틀로 호출
    return templates.TemplateResponse("main.html"
                                      ,{'request':request})

# @app.get("/")
# async def root():        # 상대의 값을 받아들이는 부분

# get("/") : 업무
# root()에서 () : 해당값