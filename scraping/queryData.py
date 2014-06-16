import sqlite3
import json


# Insert info in sqlite
conn = sqlite3.connect('/home/marcos/StocksManager/acciones.db')

for row in conn.execute('SELECT * FROM acciones'):
        print row

