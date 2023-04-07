from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#cria janela
janela = Tk()
janela.title("Estoque HotWheels- Acesso")
janela.geometry("600x300")
janela.configure(background="gray11")
janela.resizable(width=False, height=False)



#logo aleatoria
logo = PhotoImage(file="icons/logo.png")

# widgets
Leftt = Frame(janela, width=200, height=300, bg="LightBlue4", relief="raise")
Leftt.pack(side=LEFT)

Rightt = Frame(janela, width=395, height=300, bg="LightBlue4", relief="raise")
Rightt.pack(side=RIGHT)

LogoLabel = Label(Leftt, image = logo, bg="LightBlue4")
LogoLabel.place(x=50, y=100)

UserLabel = Label(Rightt, text="Usuario:", font=("Century Gothic", 20), bg="LightBlue4", fg="White")
UserLabel.place(x=5, y=100)

#entrada user e senha
EntraUser = ttk.Entry(Rightt, width=20)
EntraUser.place(x=110, y=110)

SenhaLabel = Label(Rightt, text="Senha:", font=("Century Gothic", 20), bg="LightBlue4", fg="White")
SenhaLabel.place(x=5, y=150)

SenhaUser = ttk.Entry(Rightt, width=20)
SenhaUser.place(x=110, y=160)

#botao
LoginButton = ttk.Button(Rightt, text= "Logar", width=20)
LoginButton.place(x=200, y=250)

RegisterButton = ttk.Button(Rightt, text= "Registrar", width=20)
RegisterButton.place(x=68, y=250)

janela.mainloop()
