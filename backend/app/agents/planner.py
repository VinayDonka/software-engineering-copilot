import requests
import time


def generate_plan(task: str, repo_context: str):

    prompt = f"""
You are a senior software architect.

Repository Context:

{repo_context}

Task:

{task}

IMPORTANT:

Return ONLY a numbered implementation plan.

Do NOT analyze the architecture.
Do NOT explain the repository.
Do NOT ask questions.
Do NOT provide recommendations.

Example:

1. Create auth.py
2. Add JWT middleware
3. Create login endpoint
4. Register auth router in main.py
5. Add tests

Return only the implementation plan.
"""

    start = time.time()

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:4b",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        end = time.time()

        print(
            f"Generation Time: {end - start:.2f}s"
        )

        return response.json()["response"]

    except Exception as e:

        print(f"Planner Error: {e}")

        return f"Error generating plan: {str(e)}"