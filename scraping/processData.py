import sqlite3
import json
import sys
# Entrada: Se espera el nombre del archivo que contiene la salida del scrapping

## Lee el archivo con info de las acciones
filename = sys.argv[1]
fname = '/home/marcos/StocksManager/portfolioPersonal/output/'+ filename
with open(fname) as f:
    lines = f.readlines()


# Insert info in sqlite
conn = sqlite3.connect('/home/marcos/StocksManager/acciones.db')

for l in lines:
    # Insert a row of data
    data = json.loads(l)
    insertCmd = "INSERT INTO Acciones ('Codigo','Especie','Precio','Cierre','Variacion','Fecha') VALUES ('{}', '{}', '{}', '{}', '{}', '{}')"
    insertCmd = insertCmd.format(data["Codigo"] ,data["Especie"], data["Precio"], data["Cierre"], data["Variacion"], data["Fecha"])
    conn.execute(insertCmd)
    print insertCmd

# Save (commit) the changes
conn.commit()


