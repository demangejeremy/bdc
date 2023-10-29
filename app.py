########################
# 
# La boîte du chercheur
# @DemangeJeremy
# 
########################
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import gradio as gr

# MODULES
# ...

# AUTOMATE
listApps = [
    # ...
]

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GENERATE
listAppsTxt = []
for a in listApps:
    p = a()
    listAppsTxt.append(p.info())

# ROUTES
@app.get("/")
def homepage():
    return {"status": "on"}

@app.get("/list")
def getList():
    return listAppsTxt

# AUTOMATIC ROUTING
for a in listApps:
    p = a()
    app = gr.mount_gradio_app(app, p.app(), path=p.info()["link"])