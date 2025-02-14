# Python Scripts

This repository contains a collection of Python scripts designed for automating various tasks, including system administration, file processing, and data manipulation. These scripts are intended to help system administrators, developers, and anyone looking to automate tasks using Python.

## Table of Contents

- [Introduction](#introduction)
- [Scripts](#scripts)
- [How to Use](#how-to-use)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

These Python scripts aim to simplify and automate common tasks. They provide solutions for managing files, processing data, and interacting with the operating system.  I developed these scripts to improve my own workflow and share them with the community.

## Scripts

This section provides a brief overview of each script in the repository. For more detailed information on a specific script, please refer to the script's documentation or comments within the script itself.

*   `file_manager.py`: Manages files and directories. Includes functions for creating, deleting, renaming, and moving files.
*   `data_processor.py`: Processes data from CSV or text files. Performs operations like filtering, sorting, and data transformation.
*   `system_info.py`: Retrieves system information such as OS version, CPU usage, memory usage, and disk space.
*   `network_utils.py`: Provides network utilities like pinging hosts, checking port availability, and retrieving network interface information.
*   `automation_tasks.py`: Automates various tasks, such as backing up files, sending emails, and scheduling jobs.

## How to Use

Each script includes detailed comments explaining its usage, arguments, and examples. Here are some general examples:

```bash
# Example usage of file_manager.py
python file_manager.py create_directory "new_directory"

# Example usage of data_processor.py
python data_processor.py process_csv "input.csv" "output.csv" --delimiter ","

# Example usage of system_info.py
python system_info.py get_cpu_usage

# Example usage of network_utils.py
python network_utils.py ping "[google.com](https://www.google.com/search?q=google.com)"

# Example usage of automation_tasks.py
python automation_tasks.py backup_files "/path/to/files" "/path/to/backup"
