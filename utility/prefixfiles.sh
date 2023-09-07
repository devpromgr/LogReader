#!/bin/bash

# Check if the correct number of arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <directory> <prefix>"
    exit 1
fi

# Get directory and prefix from command-line arguments
directory="$1"
prefix="$2"

# Navigate to the directory
cd "$directory" || exit

# Use a loop to rename files with the prefix
for file in *; do
    if [ -f "$file" ]; then  # Check if it's a regular file
        newname="${prefix}${file}"
        mv "$file" "$newname"
        echo "Renamed: $file -> $newname"
    fi
done

