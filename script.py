import sqlite3
from zipfile import ZipFile 

def file():
    try:
        with ZipFile('temp.apkg', 'r') as apkg_file:
            file = apkg_file.read('collection.anki2')
            with open('tempfile', 'wb') as f:
                f.write(file)

    except Exception as e:
        print(e)
        
file()

def connect(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn

def selectData(conn):
    cur = conn.cursor()
    cur.execute("SELECT flds,sfld FROM notes")
    rows = cur.fetchall()
    
    for row in rows:
        print(row[0].split("\x1f"))
        
x = connect('tempfile')
selectData(x)