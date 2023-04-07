import sqlite3

conn = sqlite3.connect('Usuarios.db')

cursor = conn.cursor()

cursor.execute(""""
CREATE TABLE IF NOT EXISTS UsuariosData (
    Id INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT
    Name TEXT NOT NULL 
);   
""")