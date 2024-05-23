#!/bin/bash
# 


# Check if the argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 directory_path"
    exit 1
fi

# Get the directory path from the argument
dir_path=$1

# Create the directory if it doesn't exist
if [ ! -d "$dir_path" ]; then
    mkdir -p "$dir_path"
fi

# Change to the directory
cd "$dir_path"

# Create some dot files
touch .file1 .file2 .file3

echo "Dot files created in $dir_path"
