import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# Load embedding model
model = None

def get_model():
    global model
    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model
# Initialize DB
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(name="repo_chunks")


def store_chunks(chunks_data):
    documents = []
    metadatas = []
    ids = []

    for i, item in enumerate(chunks_data):
        documents.append(item["chunk"])
        metadatas.append({"file_path": item["file_path"]})
        ids.append(str(i))

    embeddings = get_model().encode(documents)

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids,
        embeddings=embeddings
    )

def query_chunks(query: str, n_results=5):
    query_embedding = get_model().encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )

    return results