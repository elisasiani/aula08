from fastapi import FastAPI

from schemas import Message, UserSchema, UserPublic, UserDB

from http import HTTPStatus

app = FastAPI()

database = []


@app.get(
    '/', status_code=HTTPStatus.OK, response_model=Message
)  #'/' é um endpoint
def read_root():
    return {'message': 'Olá Mundo!', 'Outra': 'Outra Mensagem!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        id=len(database) + 1 ** user.model_dump()  # converte em lista
    )
    database.append(user_with_id)  # serve para inserir na lista
    return user_with_id
