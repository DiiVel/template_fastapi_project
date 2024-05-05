from fastapi import FastAPI
import api

app = FastAPI()

app.mount('/api', api.app)


@app.get('/ping')
async def ping():
    return {'message': 'pong'}
