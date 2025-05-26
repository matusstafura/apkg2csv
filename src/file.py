from zipfile import ZipFile
from dbconnect import DBConnect as db
import csv

def unzip_file(f):
    try:
        with ZipFile(f, 'r') as apkg_file:
            file = apkg_file.read('collection.anki21')
            with open('tempfile', 'wb') as f:
                f.write(file)

    except Exception as e:
        print(e)

def save_to_csv(f):
    try:
        with open(f, 'w', newline='', encoding='utf-8') as file:
            tempfile = db.connect('tempfile')
            writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            writer.writerow(db.header(tempfile))
            
            for i in db.values(tempfile):
                writer.writerow(i)

    except Exception as e:
        print(e)
            
