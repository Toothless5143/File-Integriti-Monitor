# File Integrity Monitor

The File Integrity Monitor is a Python script that allows you to monitor the integrity of one or more files by calculating their hash values. It compares the calculated hash values to a baseline to detect any modifications made to the monitored files.

## Description:

The File Integrity Monitor provides a simple and effective way to ensure the integrity of important files. By calculating and comparing hash values, it can detect any unauthorized changes made to the monitored files. This can be particularly useful for detecting tampering or unexpected modifications in critical system files, configuration files, or sensitive data files.

## Usage:

To use the File Integrity Monitor, follow these steps:

1. Install Python3 if you haven't already.

2. Download the `file_integrity_monitor.py` script from this repository.

3. Open a command prompt or terminal and navigate to the directory where the script is located.

4. Run the script with the following command, providing the file paths you want to monitor as command line arguments:

   ```
   python file_integrity_monitor.py file1.txt file2.txt file3.txt
   ```

   Replace `file1.txt`, `file2.txt`, etc., with the actual file paths you want to monitor.

5. The script will calculate the baseline hash values of the monitored files and start monitoring them.

6. If any of the monitored files are modified, the script will print a message indicating which file has been modified.

7. The script will continue running and monitoring the files until you manually stop it by pressing `Ctrl+C`.

## Installation:

To install and run the File Integrity Monitor, follow these steps:

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

4. Open a command prompt or terminal and navigate to the directory where the script is located.

4. Run the script with the following command, providing the file paths you want to monitor as command line arguments:

   ```
   python file_integrity_monitor.py file1.txt file2.txt file3.txt
   ```

   Replace `file1.txt`, `file2.txt`, etc., with the actual file paths you want to monitor.

5. The script will calculate the baseline hash values of the monitored files and start monitoring them.

## How the Code Works:

The File Integrity Monitor uses the SHA256 algorithm to calculate the hash values of the monitored files. It follows these steps:

1. The `get_file_hash` function calculates the hash value of a file by reading it in chunks and updating the hash digest using the SHA256 algorithm.

2. In the `main` function, the command line arguments are retrieved using `sys.argv[1:]`, excluding the script nameitself. These arguments should be the file paths that you want to monitor.

3. The baseline hash values of the monitored files are calculated and stored in the `baseline_file_hashes` dictionary.

4. The code enters an infinite loop and repeatedly calculates the current hash values of the monitored files.

5. The current hash values are compared to the baseline hash values. If any file's current hash value differs from its baseline hash value, it means the file has been modified, and a corresponding message is printed.

6. The program sleeps for 60 seconds using the `time.sleep` function to add a delay between each monitoring iteration.

7. The monitoring process continues until you manually stop the program.

8. Optional: You can pipe the output of the tool to a different file to keep track of the log.

Please note that it's important to keep the script running in the background to continuously monitor the files. You can customize the monitoring interval by adjusting the sleep duration in the code.

Feel free to modify and adapt the code according to your specific requirements.


### Conclusion:
The File Integrity Monitor is a valuable addition to any security arsenal, enabling organizations to proactively safeguard critical data, detect unauthorized changes, and maintain regulatory compliance. By leveraging its robust integrity monitoring capabilities, users can bolster their security posture and promptly respond to potential security incidents, ensuring the integrity and confidentiality of their valuable data assets.

### License:
This tool is open source and available under the [MIT License](/LICENSE).
