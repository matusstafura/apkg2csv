import os
import sys
from script import save_to_csv, file

def __main__():
    try:
        if os.path.exists(sys.argv[1]):
            apkg_file = sys.argv[1]
            csv_file = f'{apkg_file}.csv'
            file(apkg_file)
            save_to_csv(csv_file)
        else:
            exit
    except Exception as e:
        print("File required")
    
__main__()