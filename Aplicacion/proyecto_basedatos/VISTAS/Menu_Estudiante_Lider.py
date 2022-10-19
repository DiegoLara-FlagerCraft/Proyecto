def Crear_Menu_Estudiante_Lider():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont

    Menu_Lider = tk.Tk()
    Menu_Lider.config(width=1360, height=768, bg= '#7EADB0')
    Menu_Lider.title("MENU - ESTUDIANTE LIDER")
    BienvenidaLabel_Lider_Menu = tk.Label(Menu_Lider, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Lider_Menu = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Lider_Menu = tk.Label(Menu_Lider,text="BIENVENIDO LIDER",font=FontLabel_Lider_Menu,background='#7EADB0',justify=CENTER).place(x=500, y=50)

    # BOTONES
    
    def Open_Crear_Grupo():
        Menu_Lider.destroy()
        from Lider_Crear_Grupo import Crear_Lider_Crear_Grupo
        Crear_Lider_Crear_Grupo()
        
    def Open_Mi_Grupo():
        Menu_Lider.destroy()
        from Lider_Mi_Grupo import Crear_Lider_Mi_Grupo
        Crear_Lider_Mi_Grupo()
            
    def Open_Mi_Proyecto():
        Menu_Lider.destroy()
        from Lider_Mi_Proyecto import Crear_Lider_Mi_Proyecto
        Crear_Lider_Mi_Proyecto()
        
    Crear_Lider_Menu = tk.Button(Menu_Lider,text="CREAR GRUPO", font=15, bg= "#f4a020", width=30, command=Open_Crear_Grupo).place(x=450, y=200)
    GRUPO_Lider_Menu = tk.Button(Menu_Lider,text="MI GRUPO", font=15, bg= "#f4a020", width=30, command=Open_Mi_Grupo).place(x=450, y=300)
    PROYECTO_Lider_Menu = tk.Button(Menu_Lider,text="MI PROYECTO", font=15, bg= "#f4a020", width=30, command=Open_Mi_Proyecto).place(x=450, y=400)

    Menu_Lider.mainloop()