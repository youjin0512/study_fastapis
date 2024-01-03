from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

      

from starlette.responses import HTMLResponse
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# /home
# @router.get("/", response_class=HTMLResponse)
# async def home():
#     # return {"message": "home World!"}
#     # # home() 호출 -> http://192.168.10.240:8000/home
#     # return 0
#     html = "<body> <h2>It's Home</h2> </body>"
#     return html
router = APIRouter()   # APIRouter()라는 class를 router라는 변수에 담음


@router.get("/button", response_class=HTMLResponse)
async def home(Request:Request) :
    pass
    return templates.TemplateResponse(name="/gadgets/buttons.html", context={"request":Request})  # TemplateResponse라는 패키지는 진자에 의해 운영

@router.get("/cards", response_class=HTMLResponse)
async def home(Request:Request) :
    pass
    return templates.TemplateResponse(name="gadgets/cards.html", context={"request":Request})
@router.get("/colors", response_class=HTMLResponse)
async def home(Request:Request) :
    pass
    return templates.TemplateResponse(name="gadgets/colors.html", context={"request":Request})  
@router.get("/containers", response_class=HTMLResponse)
async def home(Request:Request) :
    pass
    return templates.TemplateResponse(name="containers.html", context={"request":Request})



# @get("/home/list")
# async                   # 하나의 세트로 네트워크에서 fuction 호출 시 사용