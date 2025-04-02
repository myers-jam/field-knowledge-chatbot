from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.deps import get_db
from database.models import Document
from services.embedding import embed_document
from datetime import datetime

upload_router = APIRouter()

@upload_router.post("/", summary="Upload a PDF file")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    if not file.filename.endswith(".pdf"):
        return JSONResponse(status_code=400, content={"error": "Only PDF files are supported."})

    contents = await file.read()
    await embed_document(contents, file.filename)

    # Create document entry (replace user_id with actual user if you have auth)
    doc = Document(
        filename=file.filename,
        uploaded_at=datetime.utcnow(),
        user_id=None  # set this later when user system is in place
    )
    db.add(doc)
    db.commit()

    return {"message": f"{file.filename} processed and embedded."}
