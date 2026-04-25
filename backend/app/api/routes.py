from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ingestion import clone_repo, process_repo
from app.services.vector_store import query_chunks
from app.services.llm import generate_answer


router = APIRouter()


class RepoRequest(BaseModel):
    repo_url: str


class QueryRequest(BaseModel):
    query: str


@router.post("/query")
def query_repo(request: QueryRequest):
    results = query_chunks(request.query)

    formatted = []

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    for doc, meta in zip(docs, metas):
        formatted.append({
            "file": meta["file_path"],
            "snippet": doc[:300]   # trim for readability
        })

    return {"results": formatted}

@router.post("/ingest")
def ingest_repo(request: RepoRequest):
    path = clone_repo(request.repo_url)
    total_chunks = process_repo(path)
    return {
        "message": "Repo processed",
        "total_chunks": total_chunks
    }

@router.post("/ask")
def ask_repo(request: QueryRequest):
    results = query_chunks(request.query)

    docs = results["documents"][0]

    answer = generate_answer(request.query, docs)

    return {
        "answer": answer
    }

@router.get("/health")
def health_check():
    return {"status": "ok"}

