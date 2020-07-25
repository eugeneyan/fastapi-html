from fastapi import FastAPI

from src.model import spell_number

app = FastAPI()


@app.get('/')
def read_root():
    return 'hello world'


@app.get("/rest")
def read_item(num: int):
    result = spell_number(num)
    return {"number_spelled": result}
