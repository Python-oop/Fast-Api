from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.param_functions import Depends 
from custom_log import log


router = APIRouter(prefix='/dependencies', tags=['Dependencies'],dependencies=  [Depends(log)])


def convert_params(request: Request, seperator: str):
    query = []
    for key, value in  request.query_params.items():
        query.append(f'{key}--{seperator}--{value}')
    return query    


def convert_headers(request: Request, seperator: str ='anish', query = Depends(convert_params)):
    out_headers = []
    for key, value in request.headers.items():
        out_headers.append(f'{key} -- {seperator}--{value}')
    return {
        'headers': out_headers,
        'query': query,
    }



@router.get('')
def get_items(seperator: str ,headers = Depends(convert_headers)):
    return {
        'anish': 'is a good boy',
        'headers': headers,
    }
    


@router.post('/new')
def create_items(headers = Depends(convert_headers)):
    return {
        'anish': 'is a good boy',
        'headers': headers,
    }    
    

class Account:
    def __init__(self, name: str, email:str):
        self.name = name
        self.email =email       
        
@router.post('/user')
def create_user(name: str, email: str, password: str, account: Account = Depends()):
    return {
        'name': name,
        'email': email,
    }        