from __future__ import annotations
from typing import Any, Dict, Optional
from langchain_google_genai import ChatGoogleGenerativeAI
from core.config import GEMINI_CONFIG

def get_llm() -> ChatGoogleGenerativeAI:
    """Factory function to create a Gemini LLM instance using LangChain."""
    try:
        llm = ChatGoogleGenerativeAI(
            model=GEMINI_CONFIG["model_name"] or "gemini-2.5-flash",
            temperature=GEMINI_CONFIG["temperature"],
            max_output_tokens=GEMINI_CONFIG["max_tokens"],
            **GEMINI_CONFIG["extras"],
        )
        return llm
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Gemini LLM: {e}")


if __name__ == "__main__":
    llm = get_llm()

    system_prompt = "You are a knowledgeable assistant."
    query = "Hi, can you tell me a joke?"
    messages = [
        (
            "system",
            system_prompt,
        ),
        ("human", query),
    ]

    print("🧾 Query:", query)
    print("\n💬 Model Response:\n")

    response = llm.invoke(messages)
    output = response.content
    print(output)