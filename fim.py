import hashlib
import os
import time


def get_file_hash(file_path):
    """Get the hash of a file."""
    hash_digest = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_digest.update(chunk)
    return hash_digest.hexdigest()


def main():
    """Start the file integrity monitor."""

    # Get the list of files to monitor from the command line arguments.
    files_to_monitor = sys.argv[1:]

    # Create a baseline of the file hashes.
    baseline_file_hashes = {}
    for file_path in files_to_monitor:
        baseline_file_hashes[file_path] = get_file_hash(file_path)

    # Start monitoring the files.
    while True:
        # Get the current file hashes.
        current_file_hashes = {}
        for file_path in files_to_monitor:
            current_file_hashes[file_path] = get_file_hash(file_path)

        # Compare the current file hashes to the baseline.
        for file_path, current_hash in current_file_hashes.items():
            if current_hash != baseline_file_hashes[file_path]:
                print(f"File '{file_path}' has been modified.")

        # Sleep for a specified period of time.
        time.sleep(60)


if __name__ == "__main__":
    main()
