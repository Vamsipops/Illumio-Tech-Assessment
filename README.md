
# Illumio Tech Assessment - Log Count Generator

This project provides a script to process and count log data. It computes:

1. Count of matches for each tag
2. Count of matches for each port/protocol combination

The script is designed to work on log files in the current working directory and generates output files with the required counts.

## Table of Contents
- Overview
- Input Files
- Output Files
- Assumptions
- Usage
- Requirements
- Installation
- Future Enhancements

### Overview

The code scans the current working directory for log files, processes them, and generates output files containing the following information:

- Tag counts: How often each tag appears in the logs.
- Port/Protocol counts: The count of port/protocol combinations in the logs.
The program processes all log files prefixed with log and having a .txt extension.

### Input Files

- Log files: Any text files in the current directory with names starting with log and the extension .txt are processed.
- lookup_data.csv: Contains data that maps tags and other attributes for the logs.
- protocol-numbers.csv: Contains protocol-to-number mappings (e.g., (TCP,6), (CBT,7), (EGP,8)) to map protocol numbers to text.


### Output Files

For each log file processed, a corresponding output file is generated. The output file naming convention is: output_<name_of_log_file>.txt


### Each output file contains:

Count of matches for each tag.
Count of matches for each port/protocol combination.


### Assumptions

1. All lookup data is present in the current working directory as lookup_data.csv.
2. The log file has protocols represented by numbers, and these are mapped to text using protocol-numbers.csv (also in the current directory).
3. __The log files have a consistent format__, and the protocol numbers follow standard mappings as found in protocol-numbers.csv.
4. The script assumes all log files start with the prefix log and have .txt as the file extension.

### Usage

1. Ensure the required log files, lookup_data.csv, and protocol-numbers.csv are in the current directory.
2. Run the script: python3 log_counts_generator.py
3. The script will automatically generate an output file for each log processed.

### Requirements
- Python 3.x
- Git

### Installation
1. Clone the repository by running: git clone https://github.com/yourusername/illumio-tech-assessment.git
2. Navigate to the project directory: cd illumio-tech-assessment

### Future Enhancements
- Add exception handling to manage errors such as missing files, incorrect file formats, or parsing issues more gracefully.
- Add support for different log file naming conventions.
- Introduce support for multiple log file formats (e.g., .csv, .json).
- Include unit tests for the counting logic.