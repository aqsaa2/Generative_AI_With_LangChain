import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s')


list_of_files = [
    "src\\__init__.py",
    "src\\helper.py",
    "config\\config.yaml",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research\\trials.ipynb"
]

for filepath in list_of_files:
    
    filepath = Path(filepath)
    
    filedir, filename = os.path.split(filepath)
    
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")
    
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
