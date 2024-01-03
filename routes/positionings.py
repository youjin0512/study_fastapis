from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()      # APIRouter()라는 class를 router라는 변수에 담음

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
# @router.get("/")  # / : 여기를 root라고 봄
# async def home(Request:Request) :
#     pass
#     return templates.TemplateResponse(name="homes/standards.html"       # TemplateResponse 라는 패키지는 진자에 의해 운영
#                                       , context={"request":Request})

# # /home/list
# # 어노테이션 (웹에서 업무(function) 호출) 
# @router.get("/list", response_class=HTMLResponse)        # app(fastAPI())라는 class에 get function 사용 
# async def home_list() :
#     # pass
#     # return 0
#     html = "<body> <h2>It's Home List.</h2> </body>"
#     return html

# @get("/home/list")
# async                   # 하나의 세트로 네트워크에서 fuction 호출 시 사용

@router.get("/forms",response_class=HTMLResponse)
async def form(request:Request) :
    pass 
    return templates.TemplateResponse(name="positionings/forms.html", context={'request':request})

@router.get("/grids",response_class=HTMLResponse)
async def grid(request:Request) :
    pass 
    return templates.TemplateResponse(name="positionings/grids.html", context={'request':request})

@router.get("/standards",response_class=HTMLResponse)
async def standard(request:Request) :
    pass 
    return templates.TemplateResponse(name="positionings/standards.html", context={'request':request})

@router.get("/tables",response_class=HTMLResponse)
async def table(request:Request) :
    pass 
    return templates.TemplateResponse(name="positionings/tables.html", context={'request':request})