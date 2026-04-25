import os
import subprocess
from app.services.vector_store import store_chunks

REPO_BASE_PATH = "repos"


def clone_repo(repo_url: str) -> str:
    """
    Clones a GitHub repo and returns local path
    """
    if not os.path.exists(REPO_BASE_PATH):
        os.makedirs(REPO_BASE_PATH)

    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(REPO_BASE_PATH, repo_name)

    # If already exists, skip cloning
    if os.path.exists(repo_path):
        return repo_path

    try:
        subprocess.run(
            ["git", "clone", repo_url, repo_path],
            check=True
        )
        return repo_path
    except subprocess.CalledProcessError:
        raise Exception("Failed to clone repository")

    
EXCLUDED_DIRS = {
    ".git", "node_modules", "venv", "__pycache__", "dist", "build"
}

ALLOWED_EXTENSIONS = {
    ".js", ".ts", ".py", ".java", ".md", ".json"
}


def read_repo_files(repo_path: str):
    files_data = []

    for root, dirs, files in os.walk(repo_path):
        # Remove excluded dirs
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        for file in files:
            _, ext = os.path.splitext(file)

            if ext not in ALLOWED_EXTENSIONS:
                continue

            file_path = os.path.join(root, file)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                files_data.append({
                    "file_path": file_path,
                    "content": content
                })
            except Exception:
                # Skip unreadable files
                continue

    return files_data


def chunk_text(text: str, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks



def process_repo(repo_path: str):
    files = read_repo_files(repo_path)

    chunks_data = []

    for file in files:
        chunks = chunk_text(file["content"])

        for chunk in chunks:
            chunks_data.append({
                "file_path": file["file_path"],
                "chunk": chunk
            })

    store_chunks(chunks_data)

    return len(chunks_data)