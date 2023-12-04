from fastapi import APIRouter
from models.note import Note
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from config.db import connection
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates



note = APIRouter()

templates = Jinja2Templates(directory="templates")



@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = connection.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "note": doc["note"]
        })

    print("newdocs============>",newDocs)
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})