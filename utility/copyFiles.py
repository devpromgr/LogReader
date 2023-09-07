import os
import shutil
import sys

def copy_file_to_destination(source_directory, destination_directory, source_filename):
    # Get a list of all directories in the source directory.
    directories = [d for d in os.listdir(source_directory) if os.path.isdir(os.path.join(source_directory, d))]

    # Loop through each directory and copy the source file to the destination directory with a new filename.
    for directory in directories:
        source_file = os.path.join(source_directory, directory, source_filename)

        # Check if the source file exists in the source directory.
        if os.path.isfile(source_file):
            # Define the new filename (you can customize this as needed).
            new_filename = f'{directory}_{source_filename}'
            destination_file = os.path.join(destination_directory, new_filename)

            # Copy the source file to the destination directory with the new filename.
            shutil.copyfile(source_file, destination_file)

            print(f"'{source_filename}' from '{directory}' copied to '{destination_file}'")
        else:
            print(f"'{source_filename}' not found in '{directory}'")

    print("Copy operation completed.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py source_directory destination_directory source_filename")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    source_filename = sys.argv[3]

    if not os.path.isdir(source_directory):
        print("Error: The specified source directory does not exist.")
        sys.exit(1)

    if not os.path.isdir(destination_directory):
        print("Error: The specified destination directory does not exist.")
        sys.exit(1)

    copy_file_to_destination(source_directory, destination_directory, source_filename)
