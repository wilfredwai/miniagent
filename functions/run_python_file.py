schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run or execute the file in a specified directory relative to the working directory, it will check the targeted file is a valid python file",
        "parameters": {
            "required": ["file_path"],
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The location of the .py file",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Optional command-line arguments",
                    }
                },
            },
        },
    }

import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file_path])
        if valid_target_dir != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file_path]
        if args is not None:
            command.extend(args)
        #else:
        completed = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)

        output_str = []
        if completed.returncode != 0:
            output_str.append(f'Process exited with code {completed.returncode}')
        if not completed.stdout and not completed.stderr:
            output_str.append("No output produced")
        else:
            std =[]
            std.append(completed.stdout)
            std.append(completed.stderr)
            if std[0]:
                output_str.append(f'STDOUT: {std[0]}')
            if std[1]:
                output_str.append(f'STDERR: {std[1]}')
        output = "\n".join(output_str)
        return output
    except Exception as e:
            return f"Error: executing Python file: {e}"