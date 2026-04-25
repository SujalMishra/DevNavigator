from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ingestion import clone_repo, process_repo

router = APIRouter()


class RepoRequest(BaseModel):
    repo_url: str


@router.post("/ingest")
def ingest_repo(request: RepoRequest):
    path = clone_repo(request.repo_url)
    total_chunks = process_repo(path)
    return {
        "message": "Repo processed",
        "total_chunks": total_chunks
    }

@router.get("/health")
def health_check():
    return {"status": "ok"}

