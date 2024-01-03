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
router1 = APIRouter()   # APIRouter()라는 class를 router라는 변수에 담음
router2 = APIRouter()
router3 = APIRouter()
router4 = APIRouter()

@router1.get("/")  # / : 여기를 root라고 봄
async def home(Request:Request) :
    pass
    return templates.TemplateResponse(name="gadgets/buttons.html"  # TemplateResponse 라는 패키지는 진자에 의해 운영
                                      , context={"request":Request})
@router2.get("/")  # / : 여기를 root라고 봄
async def home(Request:Request) :
    pass
    return templates.TemplateResponse(name="gadgets/cards.html"       # TemplateResponse 라는 패키지는 진자에 의해 운영
                                      , context={"request":Request})
@router3.get("/")  # / : 여기를 root라고 봄
async def home(Request:Request) :
    pass
    return templates.TemplateResponse(name="gadgets/colors.html"       # TemplateResponse 라는 패키지는 진자에 의해 운영
                                      , context={"request":Request})  
@router1.get("/")  # / : 여기를 root라고 봄
async def home(Request:Request) :
    pass
    return templates.TemplateResponse(name="containers.html"       # TemplateResponse 라는 패키지는 진자에 의해 운영
                                      , context={"request":Request})



# @get("/home/list")
# async                   # 하나의 세트로 네트워크에서 fuction 호출 시 사용