from pathlib import Path

IGNORE_DIRS = {
    "venv",
    "__pycache__",
    ".git"
}

def build_context(repo_path):

    context = []

    for file in Path(repo_path).rglob("*"):

        if any(
            ignored in file.parts
            for ignored in IGNORE_DIRS
        ):
            continue

        if file.is_file():

            try:

                if file.suffix in [
                    ".py",
                    ".js",
                    ".ts",
                    ".tsx",
                    ".json"
                ]:

                    with open(
                        file,
                        "r",
                        encoding="utf-8",
                        errors="ignore"
                    ) as f:

                        content = f.read(200)

                    context.append(
                        f"""
FILE:
{file.name}

CONTENT:
{content}
"""
                    )

            except:
                pass

    return "\n".join(context[:3])