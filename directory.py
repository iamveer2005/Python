# ek directory me kitne files hai use show karne ke liye python code
import os
# Specify the directory you want the contents to show
Directory_path = 'Problems'
# List all files and directories in the specified path
contents = os.listdir(Directory_path)
# Print each file and directory name
for item in contents:
    print(item)