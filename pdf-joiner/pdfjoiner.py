#!/usr/bin/env python
"""
PDF Joiner - Merge multiple PDF files into one
Usage: python pdfjoiner.py input1.pdf input2.pdf ... -o output.pdf
"""
import sys
import os
from pathlib import Path

try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    try:
        from PyPDF2 import PdfFileReader as PdfReader, PdfFileWriter as PdfWriter
    except ImportError:
        print("PyPDF2 not installed. Install with: pip install PyPDF2")
        sys.exit(1)


def merge_pdfs(input_files, output_path=None):
    """
    Merge multiple PDF files into one
    
    Args:
        input_files: List of input PDF file paths
        output_path: Output file path (default: merged_output.pdf)
    """
    if not input_files:
        print("No input files provided")
        sys.exit(1)
    
    # Validate input files
    for input_file in input_files:
        if not os.path.exists(input_file):
                print(f"File not found: {input_file}")
            sys.exit(1)
        if not input_file.lower().endswith('.pdf'):
                print(f"Not a PDF file: {input_file}")
            sys.exit(1)
    
            print(f"\nMerging {len(input_files)} PDF files...\n")
    
    writer = PdfWriter()
    total_pages = 0
    
    try:
        for i, input_file in enumerate(input_files, 1):
            print(f"  {i}. Adding {Path(input_file).name}...", end=" ")
            
            with open(input_file, 'rb') as f:
                reader = PdfReader(f)
                num_pages = len(reader.pages)
                
                for page_num in range(num_pages):
                    writer.add_page(reader.pages[page_num])
                
                total_pages += num_pages
                print(f"({num_pages} pages)")
        
        # Write output
        output_file = output_path or 'merged_output.pdf'
        with open(output_file, 'wb') as output:
            writer.write(output)
        
        print(f"\nSuccess! Merged {total_pages} pages into: {output_file}\n")
        
    except Exception as e:
        print(f"\nError merging PDFs: {e}")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("PDF Joiner - Merge multiple PDF files\n")
        print("Usage: python pdfjoiner.py input1.pdf input2.pdf ... [-o output.pdf]")
        print("\nExample: python pdfjoiner.py file1.pdf file2.pdf file3.pdf -o merged.pdf")
        sys.exit(1)
    
    # Parse arguments
    args = sys.argv[1:]
    output_file = None
    
    if '-o' in args:
        o_index = args.index('-o')
        if o_index + 1 < len(args):
            output_file = args[o_index + 1]
            args = args[:o_index] + args[o_index + 2:]
        else:
            print("No output file specified after -o")
            sys.exit(1)
    
    merge_pdfs(args, output_file)