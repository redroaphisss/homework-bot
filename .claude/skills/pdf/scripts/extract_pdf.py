#!/usr/bin/env python3
"""
Extract text from PDF assignment file.
"""

import PyPDF2
from pathlib import Path


def extract_pdf_text(pdf_path: Path) -> str:
    """Extract all text from a PDF file."""
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Processing PDF with {num_pages} pages...")

            for page_num, page in enumerate(reader.pages, 1):
                page_text = page.extract_text()
                if page_text:
                    text += f"\n--- Page {page_num} ---\n{page_text}\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
        raise

    return text


def main():
    """Main function."""
    pdf_path = Path("homework/Assignment 1.pdf")
    if not pdf_path.exists():
        print(f"Error: PDF file not found at {pdf_path}")
        return

    print(f"Extracting text from {pdf_path}...")
    text = extract_pdf_text(pdf_path)

    # Save to outputs directory
    output_path = Path("outputs/assignment1_text.txt")
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Text extracted and saved to {output_path}")

    # Print first few pages for preview
    print("\n=== Preview (first 2000 chars) ===")
    print(text[:2000])


if __name__ == "__main__":
    main()