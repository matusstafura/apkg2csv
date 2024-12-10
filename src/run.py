import os
import sys
from file import unzip_file, save_to_csv

def __main__():
    try:
        if os.path.exists(sys.argv[1]):
            apkg_file = sys.argv[1]
            unzip_file(apkg_file)
            save_to_csv(f'{apkg_file}.csv')
        else:
            exit
    except Exception as e:
        print("File required")
    
__main__()
