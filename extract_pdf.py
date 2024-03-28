from pypdf import PdfReader 

def extract_page_texts(file_path: str) -> list[str]:
    # Loads everything in memory - might break
    reader = PdfReader(file_path) 
    page_count = len(reader.pages)
    print(f'Extracting {page_count}')
    return [page.extract_text() for page in reader.pages]
    