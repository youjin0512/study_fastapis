from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()      # APIRouter()라는 class를 router라는 변수에 담음

from starlette.responses import HTMLResponse
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# 회원가입(forms)
@router.get("/form")
async def form(Request:Request) :
    pass
    return templates.TemplateResponse(name="/users/inserts.html", context={"request":Request})

# 로그인(insert)
@router.post("/login")
async def login(Request:Request) :
    pass
    return templates.TemplateResponse(name="/users/logins.html", context={"request":Request})

# 회원 리스트(list)
@router.get("/list")
async def list(Request:Request) :
    pass
    return templates.TemplateResponse(name="/users/lists.html", context={"request":Request})

# 회원 상세(read)
@router.get("/read/{object_id}")
async def list(Request:Request, object_id) :
    pass
    return templates.TemplateResponse(name="/users/reads.html", context={"request":Request})

# 회원상세(read) : 리스트(get), 삭제(post)
# @router.get("/read/{object:id}")
# async def read(Request:Request) :
#     pass
#     return templates.TemplateResponse(name="/users/reads.html", context={"request":Request})
# @router.post("/read/{object:id}")
# async def read(Request:Request) :
#     pass
#     return templates.TemplateResponse(name="/users/reads.html", context={"request":Request})