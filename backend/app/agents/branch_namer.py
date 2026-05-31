import requests


def generate_branch_name(
    task
):

    prompt = f"""
Create a git branch name.

Task:

{task}

Return only branch name.

Example:

feature/jwt-auth
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