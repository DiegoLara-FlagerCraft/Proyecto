def Crear_Admin_Administrar():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont
    import sqlite3 as lite

    Administrador_Administrar = tk.Tk()
    Administrador_Administrar.config(width=1360, height=768, bg= '#7EADB0')
    Administrador_Administrar.title("ADMINISTRADOR - ADMINISTRAR")
    BienvenidaLabel_Admin_Admi = tk.Label(Administrador_Administrar, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Admin_Admi = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Admin_Admi = tk.Label(Administrador_Administrar,text="BIENVENIDO ADMINISTRADOR",font=FontLabel_Admin_Admi,background='#7EADB0',justify=CENTER).place(x=500, y=50)

    # INICIATIVAS
    FontText_Admin_Admi = tkFont.Font(size = 15, weight= "bold")
    FontText_Admin_Admi2 = tkFont.Font(size = 13)
    Administrar_Admin_Admi = tk.Label(Administrador_Administrar, text="ADMINISTRAR USUARIOS:",font=FontText_Admin_Admi,background='#7EADB0').place(x=300, y=150)
    Buscar_Admin_Admi = tk.Label(Administrador_Administrar, text="BUSCAR USUARIO\nPOR MEDIO DE ID:",background='#7EADB0', font=FontText_Admin_Admi2).place(x=300, y=220)
    TexBox_Buscar_Admin_Admi = tk.Entry(Administrador_Administrar, width=100,background="#D9D9D9").place(x=490, y=230)
    Generar_Admin_Admi = tk.Label(Administrador_Administrar, text="GENERAR REPORTE:",font=FontText_Admin_Admi,background='#7EADB0').place(x=300, y=400)

    # BOTONES

    Buscar_Admin_Admi = tk.Button(text="BUSCAR", font=15, bg= "#f4a020", width=30).place(x=500, y=300)
    Generar_Admin_Admi = tk.Button(text="HAGA CLICK PARA GENERAR UN REPORTE", font=15, bg= "#f4a020", width=40).place(x=450, y=480)
    Administrador_Administrar.mainloop()