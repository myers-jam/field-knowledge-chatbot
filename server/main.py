
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.upload import upload_router
from routes.query import query_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # or ["*"] for all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router, prefix="/upload")
app.include_router(query_router, prefix="/query")

@app.get("/")
def read_root():
    return {"message": "Field Knowledge Chatbot Backend is running!"}
