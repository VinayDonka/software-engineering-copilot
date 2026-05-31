from pathlib import Path

IGNORE_DIRS = {
    "venv",
    "__pycache__",
    ".git",
    ".idea",
    ".vscode"
}

def analyze_repository(repo_path):

    files = []

    framework = "Unknown"
    language = "Unknown"

    for file in Path(repo_path).rglob("*"):

        if any(
            ignored in file.parts
            for ignored in IGNORE_DIRS
        ):
            continue

        if file.is_file():

            files.append(str(file))

            filename = file.name.lower()

            if filename == "requirements.txt":
                framework = "Python"

            if filename == "package.json":
                framework = "Node.js"

            if filename == "manage.py":
                framework = "Django"

            if filename == "main.py":
                language = "Python"

            if filename.endswith(".csproj"):
                framework = ".NET"
                language = "C#"

    return {
        "framework": framework,
        "language": language,
        "total_files": len(files),
        "sample_files": files[:10]
    }