import sqlite3
import json 
from zipfile import ZipFile

def file():
    try:
        with ZipFile('src/temp.apkg', 'r') as apkg_file:
            file = apkg_file.read('collection.anki2')
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

def saveToCsv():
    try:
        with open('src/output.csv', 'w') as f:
            tempfile = connect('tempfile')
            f.write(','.join(header(tempfile)))
            f.write('\n')
            for i in values(tempfile):
                f.write(','.join(i))
                f.write('\n')

    except Exception as e:
        print(e)
    

def __main__():
    file()
    saveToCsv()
    
__main__()