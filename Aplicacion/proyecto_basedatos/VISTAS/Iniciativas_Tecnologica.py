def Crear_Iniciativas_Tecnologicas():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont

    Iniciativas_Tecnologicas = tk.Tk()
    Iniciativas_Tecnologicas.config(width=1360, height=768, bg= '#7EADB0')
    Iniciativas_Tecnologicas.title("INICIATIVAS")
    BienvenidaLabel_Ini_Tec = tk.Label(Iniciativas_Tecnologicas, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Ini_Tec = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Ini_Tec = tk.Label(Iniciativas_Tecnologicas,text="INICIATIVAS TECNOLOGICAS",font=FontLabel_Ini_Tec,background='#7EADB0',justify=CENTER).place(x=500, y=50)

    # INICIATIVAS
    FontText_Ini_Tec = tkFont.Font(size = 12, weight= "bold")
    IniciativasDis_Ini_Tec = tk.Label(Iniciativas_Tecnologicas, text="INICIATIVAS DISPONIBLES:",font=FontText_Ini_Tec,background='#7EADB0').place(x=300, y=150)
    IniciativasPub_Ini_Tec = tk.Label(Iniciativas_Tecnologicas, text="ID     INICIATIVA #1 \nID     INICIATIVA #2 \nID     INICIATIVA #3 \nID     INICIATIVA #4", width=120, height=20, justify=LEFT).place(x=300, y=200)

    # BOTONES

    Siguiente_Ini_Tec = tk.Button(text="SIGUIENTE", font=15, bg= "#f4a020", width=20).place(x=400, y=550)
    Volver_Ini_Tec = tk.Button(text="VOLVER", font=15, bg= "#f4a020", width=20).place(x=800, y=550)

    Iniciativas_Tecnologicas.mainloop()
    
Crear_Iniciativas_Tecnologicas()