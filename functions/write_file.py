schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write or overwrite the content into a specified file relative to the working directory, it will check the targeted file is a valid or not",
        "parameters": {
            "required": ["file_path, content"],
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                "file_path": {
                    "type": "string",
                    "description": "Location of the file to be written",
                "conetent": {
                     "type": "string",
                     "description": "The content, characters will be use for write or overwrite to the file",
                }
                }
                },
            },
        },
    },
}

import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file_path])
        if valid_target_dir != working_dir_abs:
            return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        path_create = os.path.dirname(target_file_path)
        os.makedirs(f"{path_create}", exist_ok=True)
        with open(target_file_path, mode='w') as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'       
    except Exception as e:
            return f"Error: {e}"