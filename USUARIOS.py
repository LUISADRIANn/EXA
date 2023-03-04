import sqlite3
conn = sqlite3.connect("PERFIL EMPRESA SA")
c = conn.cursor()
c.execute("INSERT INTO datosest (nombre,asunto,fecha) VALUES ('DAYANA MACIAS','REPARACION DE IMPRESORA','25/1/23')")
conn.commit()
conn.close()
