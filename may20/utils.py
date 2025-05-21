# utils.py
import subprocess
import tempfile

def execute_python(code: str) -> str:
    try:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
            tmp.write(code)
            tmp_path = tmp.name
        output = subprocess.run(["python", tmp_path], capture_output=True, text=True, timeout=10)
        return output.stdout or output.stderr
    except Exception as e:
        return f"Execution Error: {str(e)}"

def lint_code(code: str) -> str:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        tmp_path = tmp.name
    try:
        result = subprocess.run(["pylint", tmp_path], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Linter Error: {str(e)}"
