from pathlib import Path


def save_code(
    repo_path: str,
    filename: str,
    code: str
):

    output_path = (
        Path(repo_path)
        / filename
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(code)

    return str(output_path)