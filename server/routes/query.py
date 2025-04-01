from fastapi import APIRouter
from pydantic import BaseModel
from services.embedding import get_embedding_for_query
from services.storage import find_similar_chunks
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

query_router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@query_router.post("/")
async def ask_question(payload: QueryRequest):
    query = payload.question
    query_vector = get_embedding_for_query(query)
    matches = find_similar_chunks(query_vector)

    # Combine top chunks into one context string
    context = "\n\n".join([f"{m['text']}" for m in matches])

    prompt = f"""
    You are an expert assistant. Use the information below to answer the question clearly and accurately.

    Document Excerpts:
    {context}

    Question: {query}
    """

    # Send to OpenAI Chat API
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who answers clearly and concisely."},
            {"role": "user", "content": prompt}
        ]
    )

    answer = completion.choices[0].message.content

    return {
        "question": query,
        "answer": answer,
        "matches_used": [m["doc"] for m in matches]
    }
