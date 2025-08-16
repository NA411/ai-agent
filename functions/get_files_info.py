import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)


def get_files_info(working_directory, directory="."):
    target_dir = os.path.join(working_directory, directory)
    if is_directory_not_in_cwd(working_directory, target_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    return "\n".join(print_files(target_dir))
    
def is_directory_not_in_cwd(working_directory, target_dir):
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.abspath(target_dir)
    return not abs_target_dir.startswith(abs_working_dir)

def print_files(target_dir):
    try:
        output_str_list = []
        for file in os.listdir(target_dir):
            path = os.path.join(target_dir, file)
            output_str_list.append(f"- {file}: file_size={os.path.getsize(path)}, is_dir={os.path.isfile(path)}")
        return output_str_list
    except Exception as e:
        return f"Error listing files: {e}"