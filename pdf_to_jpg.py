import subprocess
import glob
import os

# Get all PDF files in the current folder
folder_path = "path/to/your/folder"
pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))

for pdf in pdf_files:
    jpg = pdf.replace(".pdf", ".jpg")
    subprocess.run(["convert", pdf, jpg]) # runs the ImageMagick convert command
    print(f"Converted: {pdf} -> {jpg}")
