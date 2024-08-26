import subprocess

# Your batch commands as a string
batch_commands = """
@echo off
set /p folder_name="Enter the folder name: "
set /p folder_path="Enter the path where the folder should be created: "

mkdir "%folder_path%\%folder_name%"

echo Folder "%folder_name%" created at "%folder_path%"
pause
"""

# Run the batch commands
subprocess.run(batch_commands, shell=True, text=True)
