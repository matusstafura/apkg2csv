import sqlite3
import json 

class DBConnect:

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

