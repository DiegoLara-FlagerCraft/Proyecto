def Crear_Menu_Actualizar():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont

    Menu_Actualizar = tk.Tk()
    Menu_Actualizar.config(width=1360, height=768, bg= '#7EADB0')
    Menu_Actualizar.title("MENU - ACTUALIZAR")
    BienvenidaLabel_Actualizar_Menu = tk.Label(Menu_Actualizar, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)

    # BOTONES
    
    def Open_Actualizar_Estudiante():
        Menu_Actualizar.destroy()
        from Actualizar_Estudiantes import Crear_Actualizar_Estudiante
        Crear_Actualizar_Estudiante()
        
    def Open_Actualizar_Usuario():
        Menu_Actualizar.destroy()
        from Actualizar_Usuarios import Crear_Actualizar_Usuario
        Crear_Actualizar_Usuario()
        
    Estudiante = tk.Button(Menu_Actualizar,text="ESTUDIANTE", font=15, bg= "#f4a020", width=30, command=Open_Actualizar_Estudiante).place(x=450, y=200)
    Usuario = tk.Button(Menu_Actualizar,text="USUARIO", font=15, bg= "#f4a020", width=30, command=Open_Actualizar_Usuario).place(x=450, y=300)


    Menu_Actualizar.mainloop()
Crear_Menu_Actualizar()