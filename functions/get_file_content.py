import os
import config
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Displays the content of a specific file up to a maximum size of {config.MAX_CHARS}, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path to the specified file, relative to the working directory.",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_file_content,
    ]
)


def get_file_content(working_directory, file_path):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    print(abs_file_path)
    if is_file_not_in_cwd(working_directory, abs_file_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_file_path, "r") as f:
            return f.read(config.MAX_CHARS)
    except Exception as e:
        return f"Error: {e}"
        
def is_file_not_in_cwd(working_directory, abs_file_path):
    abs_working_dir = os.path.abspath(working_directory)
    return not abs_file_path.startswith(abs_working_dir)