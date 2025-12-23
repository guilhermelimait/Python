# 📄 PDF Joiner - Merge Multiple PDFs

Combine multiple PDF files into a single document with ease.

## 📝 Description

A Python utility that merges multiple PDF files into one consolidated document, preserving all pages and content from the source files.

## ✨ Features

- **Multiple PDF Merging**: Combine any number of PDF files
- **Page Preservation**: Maintains all pages in order
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Command-Line Interface**: Simple CLI usage
- **Memory Efficient**: Streams data to avoid memory issues

## 📋 Prerequisites

- Python 3.8+
- PDF files to merge

## 📦 Installation

```bash
# Install required package
pip install PyPDF2

# Alternative (for older versions)
pip install pyPdf
```

## 🚀 Usage

### Basic Usage

```bash
python pdfjoiner.py input1.pdf input2.pdf input3.pdf > output.pdf
```

### Windows-Specific

The script automatically handles binary mode on Windows for proper PDF output.

### Multiple Files

```bash
# Merge all PDFs in order
python pdfjoiner.py file1.pdf file2.pdf file3.pdf file4.pdf > merged.pdf
```

## 🔧 Script Functionality

The script:
1. Opens all input PDF files
2. Reads each page from all documents
3. Combines them in order
4. Writes to the output stream
5. Properly closes all file handles

```python
from PyPDF2 import PdfFileReader, PdfFileWriter

writer = PdfFileWriter()
for reader in map(PdfFileReader, input_streams):
    for n in range(reader.getNumPages()):
        writer.addPage(reader.getPage(n))
writer.write(output_stream)
```

## 💡 Use Cases

- **Document Compilation**: Combine multiple reports into one
- **Book Creation**: Merge chapters into complete book
- **Invoice Consolidation**: Combine multiple invoices
- **Archive Creation**: Create single archive from multiple documents
- **Presentation Merging**: Combine multiple presentations

## 🎯 Advanced Usage

### Python API Usage

```python
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(input_files, output_file):
    writer = PdfFileWriter()
    
    for pdf_file in input_files:
        reader = PdfFileReader(open(pdf_file, 'rb'))
        for page in range(reader.getNumPages()):
            writer.addPage(reader.getPage(page))
    
    with open(output_file, 'wb') as output:
        writer.write(output)

# Usage
merge_pdfs(['doc1.pdf', 'doc2.pdf'], 'merged.pdf')
```

### Add Page Numbers

```python
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def add_page_numbers(input_pdf, output_pdf):
    reader = PdfFileReader(open(input_pdf, 'rb'))
    writer = PdfFileWriter()
    
    for page_num in range(reader.getNumPages()):
        page = reader.getPage(page_num)
        # Add page number logic
        writer.addPage(page)
    
    with open(output_pdf, 'wb') as output:
        writer.write(output)
```

### Merge with Bookmarks

```python
def merge_with_bookmarks(pdf_list, output):
    writer = PdfFileWriter()
    
    for pdf_file in pdf_list:
        reader = PdfFileReader(open(pdf_file, 'rb'))
        start_page = writer.getNumPages()
        
        for page in range(reader.getNumPages()):
            writer.addPage(reader.getPage(page))
        
        # Add bookmark for this document
        writer.addBookmark(pdf_file, start_page)
    
    with open(output, 'wb') as out:
        writer.write(out)
```

### Selective Page Merging

```python
def merge_specific_pages(pdf_file, pages, output):
    """Merge only specific pages from a PDF"""
    reader = PdfFileReader(open(pdf_file, 'rb'))
    writer = PdfFileWriter()
    
    for page_num in pages:
        writer.addPage(reader.getPage(page_num - 1))  # 0-indexed
    
    with open(output, 'wb') as out:
        writer.write(out)

# Example: merge pages 1, 3, and 5
merge_specific_pages('input.pdf', [1, 3, 5], 'output.pdf')
```

## 📚 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| PyPDF2 | Latest | PDF reading and writing |
| pyPdf | Legacy | Alternative for older systems |

## 🐛 Troubleshooting

**Issue**: Import error
- Try: `pip install PyPDF2` (note the capitalization)
- Alternative: `pip install pyPdf` for older systems

**Issue**: Corrupted output on Windows
- Script automatically handles this with binary mode
- Ensure using Python 3.8+

**Issue**: Permission denied
- Check file permissions on input PDFs
- Ensure output path is writable
- Close PDFs in other applications

**Issue**: Memory error with large files
- Process PDFs in smaller batches
- Use streaming methods (already implemented)

## ⚠️ Limitations

- Cannot merge encrypted PDFs (password-protected)
- Form fields may not be preserved
- Some PDF features may be lost (JavaScript, etc.)
- Large files may take time to process

## 🔒 Handling Encrypted PDFs

```python
from PyPDF2 import PdfFileReader

reader = PdfFileReader(open('encrypted.pdf', 'rb'))
if reader.isEncrypted:
    reader.decrypt('password')
```

## 📄 License

MIT License - Feel free to use and modify for your projects.

---

**Part of the [Python Projects Collection](../README.md)**
