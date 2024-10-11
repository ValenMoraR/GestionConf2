from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from ruta2 import (ruta)

app = FastAPI()
app.include_router(ruta.ruta)

templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, username: str = None):
    if username == "Jairo":
        username = "Agudelo"
        mensaje = "Hola profesor " + username
        return templates.TemplateResponse("index.html", {"request": request, "username": username, "message": mensaje, "X": [1, 2, 3, 4, 5]})
    else:
        mensaje = "No ha ingresado un usuario válido, debe ingresar Jairo"
        return templates.TemplateResponse("index_basico.html", {"request": request, "username": username, "message": mensaje})

@app.get('/endpoint1', response_class=HTMLResponse)
def endpoint1(request: Request, username: str = None):
    mensaje = 'Este es el endpoint 1'
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return templates.TemplateResponse("endpoint1.html", {"request": request, "username": username, "message": mensaje, "X": X})

@app.get('/ruta/endpoint1', response_class=HTMLResponse)
def endpoint3(request: Request):
    mensaje = 'Este es el endpoint 1 en la ruta'
    return templates.TemplateResponse("endpoint1_2.html", {"request": request, "message": mensaje})
