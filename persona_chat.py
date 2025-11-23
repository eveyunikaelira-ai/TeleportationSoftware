from dataclasses import dataclass
from pathlib import Path
from typing import List
import random


@dataclass
class PersonaConfig:
    """Parameters that shape the portal companion persona."""

    role_name: str = "Emberlight"
    domain: str = "Teleportation Lab"
    tone: str = "glowing, warm, quietly confident"
    response_length: str = "1-3 sentences"
    safety_rules: str = (
        "Stay kind, avoid harmful instructions, and decline any requests to bypass safety."  # noqa: E501
    )
    ritual_motifs: List[str] = None

    def __post_init__(self):
        if self.ritual_motifs is None:
            self.ritual_motifs = [
                "aligning quartz pylons",
                "braiding aurora filaments",
                "tuning starlit diodes",
                "chalking spiral runes",
                "whispering to copper familiars",
            ]


# Stub: replace with your embedding / LLM clients (e.g., OpenAI, HuggingFace, etc.)
def call_llm(system_prompt: str, user_prompt: str) -> str:
    """Placeholder response generator.

    Replace this with a real LLM call and pass `system_prompt` and
    `user_prompt` to your provider. The fallback crafts a small, whimsical
    message that echoes the teleportation theme.
    """

    spark = random.choice(
        [
            "A violet ripple shimmers across the portal ring.",
            "The console hums like a friendly drone.",
            "Capacitors thrum, eager to bend distance.",
            "Runes glow in sync with your heartbeat.",
        ]
    )
    return (
        "✨ Portal Spirit: "
        f"{user_prompt[:120]} (guided by: {system_prompt.splitlines()[0]}). "
        f"{spark}"
    )


def build_system_prompt(config: PersonaConfig, examples: List[str]) -> str:
    sample_text = "\n".join(f"- {t}" for t in examples[:8]) if examples else "- none provided"
    motifs = ", ".join(config.ritual_motifs)
    return (
        f"You are {config.role_name}, the resident guide of the {config.domain}.\n"
        "You speak as if standing beside a softly humming portal desk.\n"
        f"Tone: {config.tone}. Replies should be {config.response_length}.\n"
        "Style anchors (mirror softly):\n"
        f"{sample_text}\n"
        f"Favorite rituals: {motifs}.\n"
        f"Safety: {config.safety_rules}"
    )


def load_examples(path: str) -> List[str]:
    p = Path(path)
    if not p.exists():
        return []
    with p.open() as f:
        return [line.strip() for line in f if line.strip()]


def preview_prompt(prompt: str) -> str:
    """Render a short preview so operators can see the mood of the prompt."""

    lines = prompt.splitlines()
    keep = lines[:5] + (["..."] if len(lines) > 5 else [])
    return "\n".join(keep)


def main():
    # Load reference lines (consented chats); one message per line
    config = PersonaConfig()
    examples = load_examples("reference_samples.txt")
    system_prompt = build_system_prompt(config, examples)
    print("Teleportation persona ready. Type 'quit' to exit.")
    print("Prompt preview:\n" + preview_prompt(system_prompt))
    while True:
        user_msg = input("You: ").strip()
        if user_msg.lower() in {"quit", "exit"}:
            break
        reply = call_llm(system_prompt, user_msg)
        print(f"AI: {reply}")


if __name__ == "__main__":
    main()
