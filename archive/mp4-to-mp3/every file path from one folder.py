import os

# how it works:
# Function to get all file paths from a given folder
def get_all_file_paths(folder):
    file_paths = []

    # os.walk generates the file names in a directory tree, including subdirectories
    for root, directories, files in os.walk(folder):
        for filename in files:
            # Create the full file path
            file_path = os.path.join(root, filename)
            file_paths.append(file_path)

    return file_paths

# Specify the folder to search
folder_path = r'C:\Users\lenni\Music\alle lieder\Motivationvideosinmp3'

# Get all file paths
all_file_paths = get_all_file_paths(folder_path)

# Print all file paths
for path in all_file_paths:
    print(path)
