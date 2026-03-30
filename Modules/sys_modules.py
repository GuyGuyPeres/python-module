import os
import sys
import subprocess
import pathlib
import platform

# Get current Working dir
print("Current folder:", os.getcwd())

# Create a Directory
# mkdir
# os.mkdir("test_folder")

# List all content
print("Files here:", os.listdir())


print(f'Python version: {sys.version}')
print(f'Platform: {sys.platform}')