import requests
import time


def generate_code(task: str, repo_context: str):

    prompt = f"""
You are a senior Python engineer.

Task:

{task}

Rules:

- Generate only Python code
- No markdown
- No explanations
- No ```python
- No comments unless necessary

Return only executable code.
"""

    start = time.time()

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:4b",
            "prompt": prompt,
            "stream": False
        }
    )

    end = time.time()

    print(
        f"Code Generation Time: {end-start:.2f}s"
    )

    return response.json()["response"]