import sqlite3
from config import config

con = config('settings.ini')

db = con.get_option('DB','db_file')

conn = sqlite3.connect(db)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   geid INTEGER,    
   fname TEXT,
   lname TEXT,
   age INTEGER,
   gender TEXT);
""")
conn.commit()

