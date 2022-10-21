def Crear_Menu_Eliminar():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont

    Menu_Eliminar = tk.Tk()
    Menu_Eliminar.config(width=1360, height=768, bg= '#7EADB0')
    Menu_Eliminar.title("MENU - Eliminar")
    BienvenidaLabel_Eliminar_Menu = tk.Label(Menu_Eliminar, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)

    # BOTONES
    
    def Open_Eliminar_Estudiante():
        Menu_Eliminar.destroy()
        from Eliminar_Estudiante import Crear_Eliminar_Estudiantes
        Crear_Eliminar_Estudiantes()
        
    def Open_Eliminar_Usuario():
        Menu_Eliminar.destroy()
        from Eliminar_Usuarios import Crear_Eliminar_Usuarios
        Crear_Eliminar_Usuarios()
        
    Estudiante = tk.Button(Menu_Eliminar,text="ESTUDIANTE", font=15, bg= "#f4a020", width=30, command=Open_Eliminar_Estudiante).place(x=450, y=200)
    Usuario = tk.Button(Menu_Eliminar,text="USUARIO", font=15, bg= "#f4a020", width=30, command=Open_Eliminar_Usuario).place(x=450, y=300)


    Menu_Eliminar.mainloop()
Crear_Menu_Eliminar()