from fastapi import APIRouter, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from custom_log import log
from schemas import ProductBase
router = APIRouter(prefix='/templates', tags=['Templates'])


templates = Jinja2Templates(directory='templates') 

@router.post('/products/{id}', response_class=HTMLResponse)
def get_product(id: str, product: ProductBase, request: Request, bt: BackgroundTasks):
    bt.add_task(log_template_call, f'product with id {id} is run on back')
    return templates.TemplateResponse(
        "product.html", {
            'request': request,
            'id': id,
            'title': product.title,
            'desc': product.description,
            'price': product.price,
        }
    )
    

def log_template_call(message: str):
    log("My api", message)   