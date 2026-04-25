import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize DB
client = chromadb.Client(
    Settings(
        persist_directory="chroma_db"
    )
)

collection = client.get_or_create_collection(name="repo_chunks")


def store_chunks(chunks_data):
    documents = []
    metadatas = []
    ids = []

    for i, item in enumerate(chunks_data):
        documents.append(item["chunk"])
        metadatas.append({"file_path": item["file_path"]})
        ids.append(str(i))

    embeddings = model.encode(documents).tolist()

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids,
        embeddings=embeddings
    )