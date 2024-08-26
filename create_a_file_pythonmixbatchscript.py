import os
import subprocess

# Define the content of the batch script
batch_script_content = """
@echo off
set /p filename=Enter the name of the file (with extension): 
echo. > %filename%
echo File "%filename%" has been created.
"""

# Get the current directory where the Python script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the path for the batch script
batch_script_path = os.path.join(current_directory, "create_file.bat")

# Write the batch script content to a file
with open(batch_script_path, "w") as batch_file:
    batch_file.write(batch_script_content)

# Run the batch script
subprocess.run([batch_script_path], shell=True)

# Optional: Clean up by deleting the batch script after execution
# os.remove(batch_script_path)
