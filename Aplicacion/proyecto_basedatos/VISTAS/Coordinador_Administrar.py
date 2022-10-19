def Crear_Coor_Administrar():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont
    import sqlite3 as lite

    Coordinador_Administrar = tk.Tk()
    Coordinador_Administrar.config(width=1360, height=768, bg= '#7EADB0')
    Coordinador_Administrar.title("COORDINADOR - ADMINISTRAR")
    BienvenidaLabel_Coor_Admi = tk.Label(Coordinador_Administrar, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Coor_Admi = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Coor_Admi = tk.Label(Coordinador_Administrar,text="BIENVENIDO COORDINADOR",font=FontLabel_Coor_Admi,background='#7EADB0',justify=CENTER).place(x=500, y=50)

    # INICIATIVAS
    FontText_Coor_Admi = tkFont.Font(size = 15, weight= "bold")
    FontText_Coor_Admi2 = tkFont.Font(size = 13)
    Administrar_Coor_Admi = tk.Label(Coordinador_Administrar, text="ADMINISTRAR USUARIOS:",font=FontText_Coor_Admi,background='#7EADB0').place(x=300, y=150)
    Buscar_Coor_Admi = tk.Label(Coordinador_Administrar, text="BUSCAR USUARIO\nPOR MEDIO DE ID:",background='#7EADB0', font=FontText_Coor_Admi2).place(x=300, y=220)
    TexBox_Buscar_Coor_Admi = tk.Entry(Coordinador_Administrar, width=100,background="#D9D9D9").place(x=490, y=230)
    Generar_Coor_Admi = tk.Label(Coordinador_Administrar, text="GENERAR REPORTE:",font=FontText_Coor_Admi,background='#7EADB0').place(x=300, y=400)

    # BOTONES

    def Volver_Menu_Coordinador():
        Coordinador_Administrar.destroy()
        from Menu_Coordinador import Crear_Menu_Coordinador
        Crear_Menu_Coordinador()

    Buscar_Coor_Admi = tk.Button(text="BUSCAR", font=15, bg= "#f4a020", width=30).place(x=500, y=300)
    Generar_Coor_Admi = tk.Button(text="HAGA CLICK PARA GENERAR UN REPORTE", font=15, bg= "#f4a020", width=40).place(x=450, y=480)
    Volver_Coordinador = tk.Button(text="VOLVER", font=15, bg= "#f4a020", width=20, command=Volver_Menu_Coordinador).place(x=550, y=650)

    Coordinador_Administrar.mainloop()