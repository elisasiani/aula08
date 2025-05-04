from fastapi import FastAPI

app = FastAPI()


@app.get('/')  #'/' é um endpoint
def read_root():
    return {'message': 'Olá mundo!'}
