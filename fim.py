import hashlib
import os
import time

def calculate_hash(file_path):
    """Calculates the SHA-256 hash of a file."""
    hash_obj = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def monitor_directory(directory_path):
    """Monitors a directory for changes in file integrity."""
    file_hashes = {}
    
    # Calculate initial hashes of all files in the directory
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = calculate_hash(file_path)
    
    while True:
        # Check for new or modified files
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                
                # Skip directories
                if os.path.isdir(file_path):
                    continue
                
                # Calculate the hash of the file
                current_hash = calculate_hash(file_path)
                
                # Compare with the previously stored hash
                if file_path not in file_hashes:
                    # New file
                    print(f'New file: {file_path}')
                    file_hashes[file_path] = current_hash
                elif file_hashes[file_path] != current_hash:
                    # Modified file
                    print(f'Modified file: {file_path}')
                    file_hashes[file_path] = current_hash
        
        # Check for deleted files
        deleted_files = []
        for file_path in file_hashes.keys():
            if not os.path.exists(file_path):
                deleted_files.append(file_path)
        
        for file_path in deleted_files:
            print(f'Deleted file: {file_path}')
            del file_hashes[file_path]
        
        # Sleep for a while before checking again
        time.sleep(60)  # Adjust the interval as needed

# Example usage
directory_to_monitor = '/path/to/directory'
monitor_directory(directory_to_monitor)
