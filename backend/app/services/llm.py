from transformers import pipeline

llm = None

def get_llm():
    global llm
    if llm is None:
        llm = pipeline(
            "text-generation",   # ✅ supported in your version
            model="distilgpt2",  # ✅ lightweight + works everywhere
        )
    return llm


def generate_answer(query: str, context_chunks: list):
    context = "\n\n".join(context_chunks[:3])  # keep small

    prompt = f"""
Context:
{context}

Question: {query}

Answer:
"""

    response = get_llm()(prompt, max_new_tokens=150)
    print("LLM response:", response)
    return response[0]["generated_text"].replace(prompt, "")