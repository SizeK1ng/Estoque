import sqlite3

conn = sqlite3.connect('Usuarios.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS UsuariosData (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);   
''')

print("Banco de Dados Conectado")
