from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from services.embedding import embed_document

upload_router = APIRouter()

@upload_router.post("/", summary="Upload a PDF file")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return JSONResponse(status_code=400, content={"error": "Only PDF files are supported."})

    contents = await file.read()
    await embed_document(contents, file.filename)

    return {"message": f"{file.filename} processed and embedded."}
