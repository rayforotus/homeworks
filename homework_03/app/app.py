from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_root():
    pass


@app.get('/ping/')
def get():
    return {'message' : 'pong'}
