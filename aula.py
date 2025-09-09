import tkinter as tk
from tkinter import messagebox

def clicar():
    print("menu clicar")

    messagebox.showwarning

janela = tk.Tk ()
janela.title("Menu bar exemplo")
janela.geometry("400x300")

menubar=tk.Menu(janela)

menu_arquivo=tk.Menu(menubar,tearoff=True)
menu_arquivo.add_command(label="início",command=clicar)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair",command=janela.quit)
menubar.add_cascade(label="Arquivo",menu=menu_arquivo)

menu_casdastro=tk.Menu(menubar,tearoff=False)
menu_casdastro.add_command(label="estante")

frame_incio=tk.Frame(janela)
lb_ola=tk.Label(frame_incio,text="bem vindo ao sistema"),
lb_ola.pack(pady=30)

janela.config(menu=menubar)


janela.mainloop()