import sys
import os


def number_of_extensions():
    try:
        dictionar = dict()
        directory = sys.argv[1]
        if os.path.exists(directory):
            if os.listdir(directory):
                for root, directories, files in os.walk(directory):
                    for filename in files:
                        file_path = os.path.join(root, filename)
                        extension = os.path.splitext(file_path)[1][0:]
                        if extension in dictionar.keys():
                            dictionar[extension] += 1
                        else:
                            dictionar[extension] = 1

                print(dictionar)
            else:
                raise ValueError(f"The directory '{directory}' is empty.")
        else:
            print("Invalid directory path")

    except FileNotFoundError:
        print("Invalid directory path")
    except PermissionError:
        print("Permission error accessing the directory.")
    except ValueError as e:
        print(e)


number_of_extensions()
# python ex4.py "C:\Users\Claudia\Desktop\an3\python\Lab6\director_cu_teste"
