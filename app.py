from fastapi import FastAPI

from aula08.schemas import Message, UserSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)  #'/' é um endpoint
def read_root():
    return {'message': 'Olá Mundo!', 'Outra': 'Outra Mensagem!'}

@app.post ('/users')
def create_user(user: UserSchema):
    return user