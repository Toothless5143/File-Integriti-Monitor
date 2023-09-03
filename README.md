# File Integrity Monitor (FIM) - Python-Based Security Tool

The File Integrity Monitor (FIM) is a powerful and versatile security tool developed in Python that allows users to monitor the integrity of files within a specified directory. Designed with professionals in mind, the FIM provides a robust solution for detecting unauthorized modifications, tampering, or deletion of critical files in real-time.

Integrity monitoring is a crucial aspect of maintaining the security and integrity of sensitive data, especially in environments where multiple users have access to critical files or when compliance with regulatory standards is required. The FIM automates the process of file integrity monitoring, reducing the risk of undetected security breaches and unauthorized access.

### Features:
1. **Hash Calculation:** The FIM utilizes the industry-standard SHA-256 algorithm to calculate the cryptographic hash of files within the monitored directory. This ensures a high level of accuracy and reliability in detecting even the slightest changes to file content.

2. **Real-Time Monitoring:** The FIM continuously monitors the specified directory, providing instant notifications of any modifications, additions, or deletions of files. By proactively detecting changes, it allows security administrators to swiftly respond to potential security incidents.

3. **Event Reporting:** The tool generates comprehensive event reports containing detailed information about detected file changes, including the file path, timestamp, and type of modification. These reports serve as crucial audit logs for compliance purposes and facilitate forensic investigations.

4. **Scalability and Flexibility:** The FIM is designed to handle large directories with numerous files and subdirectories. It supports recursive monitoring, ensuring comprehensive coverage of the entire directory structure. Additionally, the tool can be easily customized to exclude specific files or directories from monitoring based on user-defined rules.

5. **Minimal Resource Footprint:** With optimized resource utilization, the FIM operates efficiently without imposing a significant burden on system performance. The configurable monitoring interval allows for fine-tuning, striking a balance between real-time monitoring and resource consumption.

6. **User-Friendly Interface:** The FIM features a user-friendly command-line interface that simplifies configuration, monitoring, and reporting tasks. It offers clear and concise status updates, making it accessible to both security professionals and system administrators.

### Installation:
To install and use the File Integrity Monitor (FIM), follow these steps:

1. Install the required dependencies by executing the following command:
   ```
   pip install -r requirements.txt
   ```
   
2. Clone the FIM repository from GitHub using the following command:
   ```
   git clone https://github.com/Toothless5143/File-Integrity-Monitor.git
   ```

3. Navigate to the FIM directory:
   ```
   cd File-Integrity-Monitor
   ```

4. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

5. Activate the virtual environment:
   - For Windows:
     ```
     venv\Scripts\activate
     ```
   - For Linux/Mac:
     ```
     source venv/bin/activate
     ```

6. You're all set! Now you can run the FIM using the usage instructions mentioned above.

### Usage:

1. Run the FIM by executing the following command:
   ```
   python fim.py </path/to/directory>
   ```

   Replace `</path/to/directory>` with the actual directory path you want to monitor.

2. The FIM will start monitoring the specified directory, providing real-time notifications of any file modifications, additions, or deletions. Event reports will be generated, allowing you to review and respond to detected changes promptly.

### How the code works:
The `calculate_hash` function uses the `SHA-256` algorithm to calculate the hash of a file. The `monitor_directory` function accepts a directory path as an argument and continuously monitors the directory for changes in file integrity.

The script first calculates the initial hashes of all files in the directory and stores them in a dictionary. It then enters an infinite loop where it repeatedly checks for new, modified, and deleted files.

When a new file is detected, it prints a message indicating the file's path. When a file is modified, it prints a message indicating the modified file's path. Similarly, when a file is deleted, it prints a message indicating the deleted file's path.

The script sleeps for `60` seconds between each iteration of the loop to avoid excessive resource usage, but you can adjust the sleep interval as needed.

### Conclusion:
The File Integrity Monitor is a valuable addition to any security arsenal, enabling organizations to proactively safeguard critical data, detect unauthorized changes, and maintain regulatory compliance. By leveraging its robust integrity monitoring capabilities, users can bolster their security posture and promptly respond to potential security incidents, ensuring the integrity and confidentiality of their valuable data assets.

### License:
This tool is open source and available under the [MIT License](/LICENSE).
