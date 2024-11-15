Create a directory named files and place the files you want to check for duplicates inside this directory.
Dictionary for File Contents:
The file_contents dictionary stores file contents as keys, allowing the script to track unique files
Directory Traversal:
The os.walk(directory_path) function traverses through the directory and its subdirectories, retrieving the root directory, subdirectories, and filenames.
Duplicate Check and Removal:
For each file, the script constructs the full file path and reads its content.
If the content is already present in file_contents, the file is deleted using os.remove(filepath). Otherwise, the content is added to the dictionary.
