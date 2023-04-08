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

cursor.execute('''
CREATE TABLE IF NOT EXISTS Estoque (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    OwnerId INTEGER NOT NULL,
    Produto TEXT NOT NULL,
    Quantidade INTEGER NOT NULL,
    FOREIGN KEY (OwnerId) REFERENCES UsuariosData(Id)
);
''')


print("Banco de Dados Conectado")
