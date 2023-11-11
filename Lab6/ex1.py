import os
import sys


def directors_and_files():
    try:
        directory = sys.argv[1]
        file_extension = sys.argv[2]
        if not file_extension.startswith('.'):
            raise ValueError("Invalid file extension")
        if os.path.exists(directory):
            # print("Directory exists")
            for root, directories, files in os.walk(directory):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    if os.path.splitext(file_path)[1][0:] == file_extension:
                        try:
                            file_object = open(file_path, mode='r', buffering=-1, encoding=None,
                                               errors=None, newline=None, closefd=True, opener=None)
                            file_content = file_object.read()
                            print(file_content)
                        except Exception as e:
                            print(f"Error reading file '{file_path}': {e}")

        else:
            print("Invalid directory path")

    except FileNotFoundError:
        print("Invalid directory path")
    except ValueError:
        print(f"Invalid file extension")


directors_and_files()
# python ex1.py "C:\Users\Claudia\Desktop\an3\python\Lab6\director_cu_teste" ".txt"
