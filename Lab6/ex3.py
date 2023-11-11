import os
import sys


def calculate_size():
    try:
        total_size = 0
        directory = sys.argv[1]
        if os.path.exists(directory):
            for root, directories, files in os.walk(directory):
                for subdirectory in directories:
                    dir_path = os.path.join(root, subdirectory)
                    try:
                        total_size += os.path.getsize(dir_path)
                    except PermissionError:
                        print("Permission error accessing directory")

                for filename in files:
                    file_path = os.path.join(root, filename)
                    try:
                        total_size += os.path.getsize(file_path)
                    except PermissionError:
                        print("Permission error accessing file")
            print(f"Total size: {total_size} bytes")

    except FileNotFoundError:
        print("Invalid directory path")


calculate_size()

# python ex3.py "C:\Users\Claudia\Desktop\an3\python\Lab6\dir1"
