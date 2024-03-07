import os
from pdfminer.high_level import extract_text

def is_pdf_corrupted(file_path):
    try:
        text = extract_text(file_path)
    except Exception as e:
        # print(f"PDF is corrupted: {e}")
        return True
    
    # print("PDF is not corrupted.")
    return False

def check_pdfs_in_directory(directory):
    pdf_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))

    return pdf_files

if __name__ == '__main__':
    root_directory = r"D:\MyBlog\AutoFX\arxiv\2024-01-20"
    pdf_files_to_check = check_pdfs_in_directory(root_directory)

    for pdf_file_path in pdf_files_to_check:
        print(f"Checking: {pdf_file_path}")
        is_corrupted = is_pdf_corrupted(pdf_file_path)
        if is_corrupted:
            print(f"Is Corrupted: {is_corrupted}")
