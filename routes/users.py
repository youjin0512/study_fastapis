from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()      # APIRouter()라는 class를 router라는 변수에 담음

from starlette.responses import HTMLResponse
from fastapi import Request

# html 틀이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

# 회원 가입 form  /users/form -> users/inserts.html
@router.get("/form")        # app(fastAPI())라는 class에 get function 사용 
async def inserts(request:Request) :   # request : function의 변수
        return templates.TemplateResponse(name="users/inserts.html",
                                          context={"request":request})  # TemplateResponse라는 패키지는 진자에 의해 운영

# 회원 가입 /users/inserts -> users/login.html
@router.get("/insert")   
async def inserts(request:Request) : 
        pass    # biz
        return templates.TemplateResponse(name="/users/login.html",
                                          context={"request":request})  

# @get("/home/list")
# async                   # 하나의 세트로 네트워크에서 fuction 호출 시 사용


# 회원 리스트 /users/list -> users/list.html
@router.get("/list")       
async def inserts(request:Request) : 
        return templates.TemplateResponse(name="users/lists.html",
                                          context={"request":request}) 

# 회원 상세정보 /users/read -> users/reads.html
# Path parameters : /users/read/id or /users/read/unique_name      # read 클릭 했을때 특정 사람에 대해서 표현이 되야됨
@router.get("read/{object_id}")    # {object_id} -> 변수
async def inserts(request:Request, object_id) :   # object_id -> function
        return templates.TemplateResponse(name="users/reads.html",
                                          context={"request":request})