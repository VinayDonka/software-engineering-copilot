import requests


def review_code(code: str):

    prompt = f"""
Review this Python code.

Fix:

- Syntax errors
- Remove markdown fences
- Remove explanations
- Remove duplicate imports
- Complete unfinished functions

Return ONLY executable Python code.

Code:

{code}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:4b",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]