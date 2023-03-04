import sqlite3

conn = sqlite3.connect("PERFIL EMPRESA SA")

c = conn.cursor()

result = c.execute ("SELECT nombre,asunto,fecha FROM datosest")

for fila in result:

    print(fila)