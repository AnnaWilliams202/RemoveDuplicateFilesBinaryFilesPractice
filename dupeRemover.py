import os


# Function to read the entire content of a file
def read_file_content(filepath):
    with open(filepath, "rb") as f:
        return f.read()


# Directory path containing files with potential duplicates
directory_path = "files"

# Dictionary to store file contents
file_contents = {}

# Traverse through each file in the directory and its subdirectories
for root, dirs, files in os.walk(directory_path):
    for filename in files:
        filepath = os.path.join(root, filename)

        # Read the file content
        content = read_file_content(filepath)

        # Use the content as a key in the dictionary
        if content in file_contents:
            os.remove(filepath)
        else:
            file_contents[content] = filepath