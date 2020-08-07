from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

from src.model import spell_number

app = FastAPI()
templates = Jinja2Templates(directory='templates/')


def save_to_text(content, filename):
    filepath = 'data/{}.txt'.format(filename)
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath


@app.get('/')
def read_form():
    return 'hello world'

@app.get('/form')
def form_post(request: Request):
    result = 'Type a number'
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post('/form')
def form_post(request: Request, num: int = Form(...)):
    result = spell_number(num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result, 'num': num})


@app.get('/checkbox')
def form_post(request: Request):
    result = 'Type a number'
    return templates.TemplateResponse('checkbox.html', context={'request': request, 'result': result})


@app.post('/checkbox')
def form_post(request: Request, num: int = Form(...), multiply_by_2: bool = Form(False)):
    result = spell_number(num, multiply_by_2)
    return templates.TemplateResponse('checkbox.html', context={'request': request, 'result': result, 'num': num})


@app.get('/download')
def form_post(request: Request):
    result = 'Type a number'
    return templates.TemplateResponse('download.html', context={'request': request, 'result': result})


@app.post('/download')
def form_post(request: Request, num: int = Form(...), multiply_by_2: bool = Form(False), action: str = Form(...)):
    if action == 'convert':
        result = spell_number(num, multiply_by_2)
        return templates.TemplateResponse('download.html', context={'request': request, 'result': result, 'num': num})
    elif action == 'download':
        # Requires aiofiles
        result = spell_number(num, multiply_by_2)
        filepath = save_to_text(result, num)
        return FileResponse(filepath, media_type='application/octet-stream', filename='{}.txt'.format(num))
