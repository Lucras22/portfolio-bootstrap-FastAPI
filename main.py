from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 📁 Conectando a pasta 'static'
app.mount("/static", StaticFiles(directory="static"), name="static")

# 📁 Pasta dos templates
templates = Jinja2Templates(directory="templates")

@app.api_route("/", methods=["GET", "HEAD"], response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
