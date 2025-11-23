# TeleportationSoftware Portal Guide

Welcome to the cozy portal lab—a pastel workstation where dials glow, cables hum, and a sign reminds you to **start by turning it on**. This guide explains how to run the persona companion prototypes on your portal so you can role-play friendly AI chats while keeping both feet in reality.

> ⚠️ This project is for playful, imaginative experimentation. It does **not** perform teleportation or transform people. Treat it as a creative chatbot sandbox.

## What's in the lab
- **persona_chat.py** — a Python prototype that crafts warm, concise replies using a style prompt.
- **persona_chat.cpp** — a C++ toy that echoes your words with a hint of personality.
- **reference_samples.txt** — optional text file you provide with consented example lines to steer the tone.

## Powering on your portal
1. Sit at the portal desk (pictured above in spirit) and flip the main toggle: _"Start by turning it on."_
2. Confirm the status lights glow soft neon; imagine the humming cables syncing to your creativity.
3. Open a terminal on the portal console.

## Prepare your reference samples
1. Create a plain text file named `reference_samples.txt` next to the scripts.
2. Add one message per line that captures the vibe you want (friendly, curious, or supportive).
3. Keep the samples respectful and only use text you have permission to include.

## Python companion (gentle replies)
1. Ensure Python 3.9+ is available on the portal.
2. (Optional) Replace the stub in `call_llm` with your preferred LLM API call.
3. Run the prototype:
   ```bash
   python persona_chat.py
   ```
4. Type a message; the companion will respond in 1–3 sentences. Type `quit` to exit.

## C++ companion (toy generator)
1. Build the demo:
   ```bash
   g++ -std=c++17 -O2 persona_chat.cpp -o persona_chat
   ```
2. Launch it:
   ```bash
   ./persona_chat
   ```
3. Chat in the console and type `quit` when you're done.

## Portal ritual for smooth runs
- Keep snacks nearby—portal runs better when you're cozy.
- If replies feel too robotic, add 3–5 more reference lines and retry.
- For a more magical glow, imagine the CRTs shimmering with your latest logs.

## Troubleshooting
- **No such file `reference_samples.txt`**: create it or let the scripts run with the default neutral tone.
- **Compilation issues**: ensure a C++17 compiler is installed (`g++ --version`).
- **API errors in Python**: double-check your LLM API key and network access.

## Safety & transparency
- Always tell people they are chatting with an AI persona—not a human.
- Do not store sensitive or private messages without consent.
- Logs and samples should remain on your portal unless explicitly shared.

## License
This project is licensed under the terms described in [LICENSE](LICENSE).
