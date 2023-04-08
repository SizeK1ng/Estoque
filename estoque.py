import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3

# Função para fazer a conexão com o banco de dados
def connect():
    conn = sqlite3.connect('Usuarios.db')
    cursor = conn.cursor()
    return conn, cursor

# Função para fechar a conexão com o banco de dados
def close(conn):
    conn.commit()
    conn.close()

# Função para adicionar um novo carrinho
def add_to_cart():
    global cart_image_entry, cart_code_entry

    name = cart_name_entry.get()
    desc = cart_desc_entry.get('1.0', 'end-1c')
    user = user_entry.get()

    root = tk.Tk()
    root.title('Estoque')

    cart_image_entry = tk.Entry(root)
    cart_image_entry.grid(row=4, column=1, padx=5, pady=5)

    cart_code_entry = tk.Entry(root)
    cart_code_entry.grid(row=3, column=1, padx=5, pady=5)

    if name == '':
        messagebox.showerror('Erro', 'Por favor, insira o nome do carrinho')
    elif desc == '':
        messagebox.showerror('Erro', 'Por favor, insira a descrição do carrinho')
    else:
        conn, cursor = connect()
        cursor.execute('INSERT INTO Carrinho (OwnerId, Name, Description) VALUES (?, ?, ?)', (get_user_id(user), name, desc))
        cart_id = cursor.lastrowid
        close(conn)
        messagebox.showinfo('Sucesso', 'Carrinho adicionado com sucesso')

        # Adiciona a imagem do carrinho, se houver
        image_path = cart_image_entry.get()
        if image_path != '':
            add_image(cart_id, image_path)

# Função para pesquisar um carrinho
def search_cart(cart_image_entry, cart_code_entry):
    code = cart_code_entry.get()
    user = user_entry.get()

    if code == '':
        messagebox.showerror('Erro', 'Por favor, insira o código do carrinho')
    else:
        conn, cursor = connect()
        cursor.execute('SELECT * FROM Carrinho WHERE OwnerId = ? AND Code = ?', (get_user_id(user), code))
        cart = cursor.fetchone()
        close(conn)

        if cart is None:
            messagebox.showerror('Erro', 'Carrinho não encontrado')
        else:
            messagebox.showinfo('Sucesso', f'Nome: {cart[2]}\nDescrição: {cart[3]}')

# Função para adicionar uma imagem ao carrinho
def add_image(cart_id, image_path):
    with open(image_path, 'rb') as f:
        img_data = f.read()

    conn, cursor = connect()
    cursor.execute('INSERT INTO ImagemCarrinho (CarrinhoId, Imagem) VALUES (?, ?)', (cart_id, img_data))
    close(conn)

# Função para obter o id do usuário a partir do nome de usuário
# Função para obter o id do usuário a partir do nome de usuário
def get_user_id(username):
    conn, cursor = connect()
    cursor.execute('SELECT Id FROM UsuariosData WHERE User = ?', (username,))
    user_id = cursor.fetchone()[0]
    close(conn)
    return user_id

# Função para listar os carrinhos do usuário
def list_carts():
    user = user_entry.get()

    conn, cursor = connect()
    cursor.execute('SELECT * FROM Carrinho WHERE OwnerId = ?', (get_user_id(user),))
    carts = cursor.fetchall()
    close(conn)

    if not carts:
        messagebox.showinfo('Informação', 'Você ainda não possui carrinhos registrados')
    else:
        cart_list = ''
        for cart in carts:
            cart_list += f'Nome: {cart[2]}\nDescrição: {cart[3]}\n\n'
        messagebox.showinfo('Carrinhos Registrados', cart_list)

# Interface gráfica
root = tk.Tk()
root.title('Estoque')

## Labels e Entradas de texto
tk.Label(root, text='Nome de Usuário:').grid(row=0, column=0, padx=5, pady=5)
user_entry = tk.Entry(root)
user_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text='Nome do Carrinho:').grid(row=1, column=0, padx=5, pady=5)
cart_name_entry = tk.Entry(root)
cart_name_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text='Descrição:').grid(row=2, column=0, padx=5, pady=5)
cart_desc_entry = tk.Text(root, height=4)
cart_desc_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text='Código do Carrinho:').grid(row=3, column=0, padx=5, pady=5)
cart_code_entry = tk.Entry(root)
cart_code_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text='Imagem do Carrinho:').grid(row=4, column=0, padx=5, pady=5)
cart_image_entry = tk.Entry(root)
cart_image_entry.grid(row=4, column=1, padx=5, pady=5)

#Botões
tk.Button(root, text='Adicionar Carrinho', command=add_to_cart).grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text='Pesquisar Carrinho', command=search_cart).grid(row=5, column=1, padx=5, pady=5)
tk.Button(root, text='Listar Carrinhos', command=list_carts).grid(row=6, column=0, padx=5, pady=5)

root.mainloop() # loop principal do tkinter para exibir a janela interativa.