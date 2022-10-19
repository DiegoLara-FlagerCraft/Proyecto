def Crear_Coor_Iniciativas():    
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont
    import sqlite3 as lite

    Coordinador_Iniciativas = tk.Tk()
    Coordinador_Iniciativas.config(width=1360, height=768, bg= '#7EADB0')
    Coordinador_Iniciativas.title("COORDINADOR - INICIATIVAS")
    BienvenidaLabel_Coor_Ini = tk.Label(Coordinador_Iniciativas, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Coor_Ini = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Coor_Ini = tk.Label(Coordinador_Iniciativas,text="BIENVENIDO COORDINADOR",font=FontLabel_Coor_Ini,background='#7EADB0',justify=CENTER).place(x=500, y=50)

    # INICIATIVAS
    FontText_Coor_Ini = tkFont.Font(size = 12, weight= "bold")
    Peticiones_Coor_Ini = tk.Label(Coordinador_Iniciativas, text="PETICION INICIATIVAS:",font=FontText_Coor_Ini,background='#7EADB0').place(x=300, y=150)
    Combox_Peticiones_Coor_Ini = ttk.Combobox(state="readonly", values=["INICIATIVA #1", "INICIATIVA #2"],background='#D9D9D9',width=60).place(x=300, y=180)
    Estado_Coor_Ini = tk.Label(Coordinador_Iniciativas, text="ESTADO:",font=FontText_Coor_Ini,background='#7EADB0').place(x=900, y=150)
    Combox_Estado_Coor_Ini = ttk.Combobox(state="readonly", values=["APROBADO", "RECHAZADO"],background='#D9D9D9',width=30).place(x=900, y=180)

    # BOTONES

    def Volver_Menu_Coordinador():
        Coordinador_Iniciativas.destroy()
        from Menu_Coordinador import Crear_Menu_Coordinador
        Crear_Menu_Coordinador()

    Enviar_Coor_Ini = tk.Button(text="ENVIAR", font=15, bg= "#f4a020", width=30).place(x=500, y=550)
    Volver_Coordinador = tk.Button(text="VOLVER", font=15, bg= "#f4a020", width=20, command=Volver_Menu_Coordinador).place(x=550, y=650)

    Coordinador_Iniciativas.mainloop()