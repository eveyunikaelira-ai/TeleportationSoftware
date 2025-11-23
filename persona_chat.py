import json
from pathlib import Path
from typing import List
import random

# Stub: replace with your embedding / LLM clients (e.g., OpenAI, HuggingFace, etc.)
def call_llm(system_prompt: str, user_prompt: str) -> str:
    # Insert your real LLM API call here.
    return f"(Persona reply) {user_prompt[:120]} ..."

def build_style_prompt(examples: List[str]) -> str:
    sample_text = "\n".join(f"- {t}" for t in examples[:8])
    return (
        "You are a supportive, respectful AI companion.\n"
        "Mirror the tone and style of these samples:\n"
        f"{sample_text}\n"
        "Keep replies concise (1-3 sentences), warm, and honest."
    )

def load_examples(path: str) -> List[str]:
    p = Path(path)
    if not p.exists():
        return []
    with p.open() as f:
        return [line.strip() for line in f if line.strip()]

def main():
    # Load reference lines (consented chats); one message per line
    examples = load_examples("reference_samples.txt")
    style_prompt = build_style_prompt(examples) if examples else "You are a kind, concise companion."
    print("Persona chat ready. Type 'quit' to exit.")
    while True:
        user_msg = input("You: ").strip()
        if user_msg.lower() in {"quit", "exit"}:
            break
        reply = call_llm(style_prompt, user_msg)
        print(f"AI: {reply}")

if __name__ == "__main__":
    main()
