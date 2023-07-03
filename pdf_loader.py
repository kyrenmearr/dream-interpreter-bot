from pathlib import Path
from llama_index import download_loader

PDFReader = download_loader('PDFReader')

loader = PDFReader()
documents = loader.load_data(file=Path('data/dreams.pdf'))