import os

FOLDER = "X:/full/path/to/folder"

def main():
    count=0 
    for i in os.listdir(FOLDER):
        count+=1
        x, file_extension = os.path.splitext(i)
        new_name = f"{count}{file_extension}"
        src = f"{FOLDER}/{i}"
        dst = f"{FOLDER}/{new_name}"
        os.rename(src, dst)
        print(f"{src} renamed to {dst}")

if __name__ == "__main__":
    main()