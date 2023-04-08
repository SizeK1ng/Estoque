from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import data
# cria janela
janela = Tk()
janela.title("Estoque HotWheels- Acesso")
janela.geometry("600x300")
janela.configure(background="gray11")
janela.resizable(width=False, height=False)


# logo aleatoria
logo = PhotoImage(file="icons/logo.png")

# widgets
Leftt = Frame(janela, width=200, height=300, bg="LightBlue4", relief="raise")
Leftt.pack(side=LEFT)

Rightt = Frame(janela, width=395, height=300, bg="LightBlue4", relief="raise")
Rightt.pack(side=RIGHT)

LogoLabel = Label(Leftt, image=logo, bg="LightBlue4")
LogoLabel.place(x=50, y=100)


UserLabel = Label(Rightt, text="Nick:", font=("Century Gothic", 20), bg="LightBlue4", fg="White")
UserLabel.place(x=5, y=100)

# entrada user e senha
EntraUser = ttk.Entry(Rightt, width=20)
EntraUser.place(x=110, y=110)

SenhaLabel = Label(Rightt, text="Senha:", font=(
    "Century Gothic", 20), bg="LightBlue4", fg="White")
SenhaLabel.place(x=5, y=150)

SenhaUser = ttk.Entry(Rightt, width=20, show="*")
SenhaUser.place(x=110, y=160)

# botoes
LoginButton = ttk.Button(Rightt, text="Logar", width=20)
LoginButton.place(x=200, y=250)


def Register():
    # remove widgets de login
    LoginButton.place(x=50000)
    RegisterButton.place(x=50000)
# widgets de cadastro
    NomeLabel = Label(Rightt, text="Nome: ", font=(
        "Century Gothic", 20), bg="LightBlue4", fg="white")
    NomeLabel.place(x=5, y=60)

    NomeEntry = ttk.Entry(Rightt, width=20)
    NomeEntry.place(x=110, y=70)

    def RegisterToDataBase():
        Nome = NomeEntry.get()
        Nick = EntraUser.get()
        Senha = SenhaUser.get()
        data.cursor.execute('''
        INSERT INTO UsuariosData(Name, User, Password) VALUES(?, ?, ?)
        ''', (Nome, Nick, Senha)) 
        data.conn.commit()
        #caixa de mensagem
        messagebox.showinfo(title="Registro info", message="Registrado com sucesso")

    Register = ttk.Button(Rightt, text="Registrar", width=20, command= RegisterToDataBase)
    Register.place(x=200, y=250)

    def BackToLogin():
        # remove a caixa de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        # traz as caixas de cadastro
        LoginButton.place(x=200, y=250)
        RegisterButton.place(x=68, y=250)

    Back = ttk.Button(Rightt, text="Voltar", width=20, command=BackToLogin)
    Back.place(x=68, y=250)


RegisterButton = ttk.Button(
    Rightt, text="Registrar", width=20, command=Register)
RegisterButton.place(x=68, y=250)


janela.mainloop()
