import sqlite3
import json 
import csv
from zipfile import ZipFile

def file(f):
    try:
        with ZipFile(f, 'r') as apkg_file:
            file = apkg_file.read('collection.anki21')
            with open('tempfile', 'wb') as f:
                f.write(file)

    except Exception as e:
        print(e)
        
def connect(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn

def header(conn):
    cur = conn.cursor()
    cur.execute("SELECT models FROM col")
    rows = cur.fetchall()
    
    items = json.loads(rows[0][0])
    items = items.pop(list(items)[0])
    
    return [_['name'] for _ in items['flds']]

def values(conn):
    cur = conn.cursor()
    cur.execute("SELECT flds,sfld FROM notes")
    rows = cur.fetchall()
    
    return [_[0].split("\x1f") for _ in rows]

def save_to_csv(f):
    try:
        with open(f, 'w', newline='') as file:
            tempfile = connect('tempfile')
            writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            writer.writerow(header(tempfile))
            
            for i in values(tempfile):
                writer.writerow(i)

    except Exception as e:
        print(e)
            
