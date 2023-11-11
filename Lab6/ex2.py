import os
import sys


def renaming():
    try:
        count = 1
        directory = sys.argv[1]
        if os.path.exists(directory):
            for root, directories, files in os.walk(directory):
                for filename in files:
                    try:
                        old_path = os.path.join(root, filename)
                        new_name = "file" + str(count)
                        new_path = os.path.join(root, new_name)
                        os.rename(old_path, new_path)
                        count += 1
                    except FileExistsError:
                        print("File name already exists")

    except FileNotFoundError:
        print("Invalid directory path")


renaming()
# python ex2.py "C:\Users\Claudia\Desktop\an3\python\Lab6\director_cu_teste"
