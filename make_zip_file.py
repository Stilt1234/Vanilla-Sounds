import os
import zipfile

def make_zip():
    with zipfile.ZipFile(os.path.join(os.getcwd(), "Vanilla Sounds.zip"), 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for root, dirs, files in os.walk(os.path.join(os.getcwd(), "Vanilla Sounds")):
                for file in files:
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, os.path.join(os.getcwd(), "Vanilla Sounds"))
                    zf.write(full_path, rel_path)