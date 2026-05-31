import requests


def generate_filename(task: str):

    prompt = f"""
Generate a Python filename for:

{task}

Return only filename.

Example:
jwt_middleware.py
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:4b",
            "prompt": prompt,
            "stream": False
        }
    )

    return (
        response.json()["response"]
        .strip()
        .replace("`", "")
    )