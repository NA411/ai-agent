import os, subprocess, config
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
     description=(
        "Executes a Python (.py) file located within the working directory using the 'uv' runtime. "
        "Captures and returns standard output and error streams. "
        "Rejects execution if the file is outside the working directory or not a valid Python file."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path to the specified file to write the content to, relative to the working directory.",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_run_python_file,
    ]
)


def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        f'Error: "{file_path}" is not a Python file.'
    try:
        
        commands = ["uv", "run", abs_file_path]
        if args:
            commands.extend(args)

        completed_process = subprocess.run(
            commands,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=config.SUBPROCESS_TIMEOUT_TIME,
        )
        results = []
        results.append(f"STDERR: {completed_process.stderr}")
        if completed_process.stdout == None:
            results.append("No output produced.")
        else:
            results.append(f"STDOUT: {completed_process.stdout}")
            results.append("---")
        if completed_process.returncode != 0:
            results.append(f"Process exited with code {completed_process.returncode}")
        results.append("---")
        return "\n".join(results)
    except Exception as e:
        return f"Error: executing Python file: {e}"
