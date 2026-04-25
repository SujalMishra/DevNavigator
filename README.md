# Dev Navigator — AI Codebase Assistant

Dev Navigator is an AI-powered system that helps developers **understand any GitHub repository instantly**.

Provide a repository URL → ask questions → get **context-aware answers from the codebase**.

---

## 🔥 What Problem It Solves

Understanding large codebases is slow:

* No documentation ❌
* Poor onboarding ❌
* Hard to trace logic ❌

👉 Dev Navigator solves this by acting like a **ChatGPT for your repo**.

---

## 🧠 Core Idea

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline:

* Convert code into embeddings
* Store in vector database
* Retrieve relevant context
* Generate answers using LLM
  
---

## ⚙️ Detailed Flow

```text
1. User provides GitHub repo URL
2. Backend clones the repository
3. Files are read and split into chunks
4. Each chunk is converted into embeddings
5. Embeddings stored in vector DB (Chroma)
6. User asks a question
7. Query is embedded into vector space
8. Similar chunks are retrieved
9. LLM generates answer using retrieved context
```

---

## 🧱 Architecture Breakdown

### 🔹 Ingestion Pipeline

* Clone repository
* Read files
* Chunk code
* Generate embeddings
* Store in DB

### 🔹 Query Pipeline

* Accept user query
* Convert to embedding
* Retrieve top-k similar chunks
* Pass to LLM
* Generate final response

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Uvicorn

### AI / ML

* Sentence Transformers (Embeddings)
* Local LLM (via Ollama / Transformers)

### Database

* ChromaDB (Vector Store)

### Utilities

* Python
* GitPython

---

## 📂 Project Structure

```
Dev-Navigator/
│
├── backend/
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── services/     # ingestion, vector store, llm
│   │   ├── main.py       # FastAPI entry point
│   │
│   ├── chroma_db/        # vector storage
│   ├── venv/
│
├── frontend/             # (planned)
```

---

## 🚀 Getting Started

### 1. Clone repo

```bash
git clone <your-repo-url>
cd Dev-Navigator/backend
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run backend

```bash
uvicorn app.main:app --reload
```

---

### 5. Open API docs

```
http://127.0.0.1:8000/docs
```

---

## 🔌 API Endpoints

### 📥 Ingest Repository

```http
POST /ingest
```

```json
{
  "repo_url": "https://github.com/user/repo"
}
```

---

### 🔍 Query (Raw Retrieval)

```http
POST /query
```

---

### 🤖 Ask AI

```http
POST /ask
```

```json
{
  "query": "Where is authentication handled?"
}
```

---

## 🧠 Key Concepts

* Retrieval-Augmented Generation (RAG)
* Vector Embeddings
* Semantic Search
* LLM Integration
* Prompt Engineering

---

## 🔮 Future Improvements

* Better LLM (Mistral / LLaMA via Ollama)
* Streaming responses
* Multi-repo support
* Frontend UI (React)
* Code navigation + highlighting

---

## 👨‍💻 Author

Sujal Mishra

---

## ⭐ Show Support

If you like this project, consider giving it a star ⭐
