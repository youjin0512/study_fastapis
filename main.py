from fastapi import FastAPI
app = FastAPI()
from routes.gadgets import router as event_router
from routes.positionings import router as second_router
from fastapi import Request
from fastapi.templating import Jinja2Templates
from routes.users import router as users_router
from routes.homes import router as home_router

app.include_router(home_router, prefix="/home")
app.include_router(event_router, prefix="/gadgets")
app.include_router(second_router, prefix="/positionings")
app.include_router(users_router, prefix="/users")

# html 들이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root(Request:Request):
    # return {"message": "youjin World"}
    return templates.TemplateResponse("main.html",
                                      {'request':Request})

@app.get("/index")
async def root(Request:Request):
    # return {"message": "youjin World"}
    return templates.TemplateResponse("index.html",
                                      {'request':Request})
