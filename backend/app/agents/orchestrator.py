from app.agents.context_builder import build_context
from app.agents.planner import generate_plan
from app.agents.code_generator import generate_code
from app.agents.file_writer import save_code
from app.agents.file_namer import generate_filename
from app.agents.git_manager import commit_changes
from app.agents.reviewer import review_code
from app.agents.branch_manager import create_branch
from app.agents.branch_namer import generate_branch_name

from pathlib import Path

from app.agents.validator import (
    validate_python
)

def run_agent(repo_path: str, task: str):
    from pathlib import Path

    project_root = str(
        Path(repo_path).parent
    )

    branch_name = generate_branch_name(
        task
    )

    create_branch(
        project_root,
        branch_name
    )
    # Build repository context
    context = build_context(
        repo_path
    )

    # Generate plan
    plan = generate_plan(
        task,
        context
    )

    # Generate filename
    filename = generate_filename(
        task
    )

    # Generate code
    generated_code = generate_code(
        task,
        context
    )

    reviewed_code = review_code(
        generated_code
    )
    
    valid, error = validate_python(
        reviewed_code
    )

    # Clean markdown wrappers
    reviewed_code = reviewed_code.replace(
        "```python",
        ""
    )

    reviewed_code = reviewed_code.replace(
        "```",
        ""
    )

    saved_path = save_code(
        repo_path,
        filename,
        reviewed_code
    )


    project_root = str(
    Path(repo_path).parent
    )
    
    # Commit changes automatically
    commit_sha = commit_changes(
    project_root,
    f"AI Agent: {task}"
    )
    
    branch_name = generate_branch_name(
        task
    )

    create_branch(
        project_root,
        branch_name
    )
    
    return {
        "task": task,
        "branch": branch_name,
        "filename": filename,
        "plan": plan,
        "saved_to": saved_path,
        "commit_sha": commit_sha,
        "line_count": len(
            reviewed_code.splitlines()
        ),
        "code_lines": reviewed_code.splitlines()
        
    }
    
    if not valid:

        return {
            "task": task,
            "error": error,
            "status": "validation_failed"
        }
    

