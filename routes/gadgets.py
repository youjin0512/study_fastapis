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


@router.get("/buttons", response_class=HTMLResponse)
async def buttons(Request:Request) :
    pass
    return templates.TemplateResponse(name="/gadgets/buttons.html", context={"request":Request})  # TemplateResponse라는 패키지는 진자에 의해 운영

@router.get("/cards")   # cards_GET 방식
# Request = Request (query_parameters)
async def cards(Request:Request) :
    ## 디버깅콘솔창에서 나온 내용 -> 몽고DB에 입력 가능
    # Request.query_params
    # QueryParams('name=youjin&email=kelly.youjin.kim%40gmail.com')
    
    # dict(Request.query_params)
    # {'name': 'youjin', 'email': 'kelly.youjin.kim@gmail.com'}  # request class : '요청'을 받는 묶음
    return templates.TemplateResponse(name="gadgets/cards.html", context={"request":Request})

@router.post("/cards")   # cards_POST 방식
async def cards_post(Request:Request) :
    ## 디버깅콘솔창에서 나온 내용 -> 몽고DB에 입력 가능
    # Request.query_params
    # QueryParams('')

    # await Request.form()
    # FormData([('name', 'youjin'), ('email', 'kelly.youjin.kim@gmail.com')])

    # dict(await Request.form())
    # {'name': 'youjin', 'email': 'kelly.youjin.kim@gmail.com'}

    # form_datas = await Request.form()
    # dict(form_datas)
    return templates.TemplateResponse(name="gadgets/cards.html", context={"request":Request})

@router.get("/colors", response_class=HTMLResponse)
async def colors(Request:Request) :
    pass
    return templates.TemplateResponse(name="gadgets/colors.html", context={"request":Request})  

@router.get("/containers", response_class=HTMLResponse)
async def containers(Request:Request) :
    pass
    return templates.TemplateResponse(name="gadgets/containers.html", context={"request":Request})



# @get("/home/list")
# async                   # 하나의 세트로 네트워크에서 fuction 호출 시 사용