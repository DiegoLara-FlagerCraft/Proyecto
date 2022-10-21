def Crear_Menu_Coordinador():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont

    Menu_Coordinador = tk.Tk()
    Menu_Coordinador.config(width=1360, height=768, bg= '#7EADB0')
    Menu_Coordinador.title("MENU - COORDINADOR")
    BienvenidaLabel_Coordinador_Menu = tk.Label(Menu_Coordinador, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Coordinador_Menu = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Coordinador_Menu = tk.Label(Menu_Coordinador,text="BIENVENIDO COORDINADOR",font=FontLabel_Coordinador_Menu,background='#7EADB0',justify=CENTER).place(x=500, y=50)

    # BOTONES
    
    def Open_Coordinador_Administrar():
        Menu_Coordinador.destroy()
        from Coordinador_Administrar import Crear_Coor_Administrar
        Crear_Coor_Administrar()
        
    def Open_Coordinador_Iniciativas():
        Menu_Coordinador.destroy()
        from Coordinador_Iniciativas import Crear_Coor_Iniciativas
        Crear_Coor_Iniciativas()
            
    def Open_Coordinador_Permisos():
        Menu_Coordinador.destroy()
        from Coordinador_Permisos_Lider import Crear_Coor_Permisos_Lider
        Crear_Coor_Permisos_Lider()
        
    def Open_Menu_Actualizar():
        Menu_Coordinador.destroy()
        from Menu_Actualizar import Crear_Menu_Actualizar
        Crear_Menu_Actualizar()
            
    def Open_Menu_Eliminar():
        Menu_Coordinador.destroy()
        from Menu_Eliminar import Crear_Menu_Eliminar
        Crear_Menu_Eliminar()
        
    def Open_Eliminar_Iniciativa():
        Menu_Coordinador.destroy()
        from Eliminar_Iniciativa import Crear_Eliminar_Iniciativa
        Crear_Eliminar_Iniciativa()
        
        
    Administrar_Coordinador_Menu = tk.Button(Menu_Coordinador,text="ADMINISTRAR", font=15, bg= "#f4a020", width=30, command=Open_Coordinador_Administrar).place(x=450, y=200)
    Iniciativas_Coordinador_Menu = tk.Button(Menu_Coordinador,text="INICIATIVAS", font=15, bg= "#f4a020", width=30, command=Open_Coordinador_Iniciativas).place(x=450, y=250)
    Permisos_Coordinador_Menu = tk.Button(Menu_Coordinador,text="PERMISOS", font=15, bg= "#f4a020", width=30, command=Open_Coordinador_Permisos).place(x=450, y=300)
    Actuarizar_Coordinador_Menu = tk.Button(Menu_Coordinador,text="ACTUALIZAR USUARIOS", font=15, bg= "#f4a020", width=30, command=Open_Menu_Actualizar).place(x=450, y=350)
    Eliminar_Coordinador_Menu = tk.Button(Menu_Coordinador,text="ELIMINAR USUARIOS", font=15, bg= "#f4a020", width=30, command=Open_Menu_Eliminar).place(x=450, y=400)
    Eliminar_Iniciativas_Coordinador_Menu = tk.Button(Menu_Coordinador, text="ELIMINAR INICIATIVAS", font=15, bg="#f4a020", width=30, command=Open_Eliminar_Iniciativa).place(x=450, y=450)


    Menu_Coordinador.mainloop()
Crear_Menu_Coordinador()