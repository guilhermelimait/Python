def merge_specific_pages(pdf_file, pages, output):
# PDF Joiner - Merge Multiple PDFs

Combine multiple PDF files into a single document with a simple CLI.

## Description

Python utility that merges PDFs using PyPDF2. Updated to the modern `PdfReader`/`PdfWriter` API and supports an `-o` flag for output filename.

## Features

- Merge any number of PDF files in order
- Validates input existence and file type
- Command-line output selection with `-o`
- Clear progress messages with page counts

## Prerequisites

- Python 3.8+
- PyPDF2 installed

## Installation

```bash
pip install PyPDF2
```

## Usage

```bash
# Basic merge
python pdfjoiner.py file1.pdf file2.pdf file3.pdf -o merged.pdf

# If -o is omitted, output defaults to merged_output.pdf
```

## Behavior

- Rejects missing files or non-PDF inputs
- Writes to a new file; no stdout piping is required
- Reports how many pages were merged

## Dependencies

| Package | Purpose                |
|---------|------------------------|
| PyPDF2  | PDF reading and writing|

## Notes

- Encrypted/password-protected PDFs are not supported.
- For very large files, ensure adequate disk space for the output file.

---

Part of the [Python Projects Collection](../README.md)

## 📄 License

MIT License - Feel free to use and modify for your projects.

---

**Part of the [Python Projects Collection](../README.md)**
