def Crear_Menu_Admin():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont

    Menu_Admin = tk.Tk()
    Menu_Admin.config(width=1360, height=768, bg= '#7EADB0')
    Menu_Admin.title("MENU - ADMIN")
    BienvenidaLabel_Admin_Menu = tk.Label(Menu_Admin, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Admin_Menu = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Admin_Menu = tk.Label(Menu_Admin,text="BIENVENIDO ADMINISTRADOR",font=FontLabel_Admin_Menu,background='#7EADB0',justify=CENTER).place(x=500, y=50)

    # BOTONES
    
    def Open_Admin_Administrar():
        Menu_Admin.destroy()
        from Administrador_Administrar import Crear_Admin_Administrar
        Crear_Admin_Administrar()
        
    def Open_Menu_Actualizar():
        Menu_Admin.destroy()
        from Menu_Actualizar import Crear_Menu_Actualizar
        Crear_Menu_Actualizar()
            
    def Open_Menu_Eliminar():
        Menu_Admin.destroy()
        from Menu_Eliminar import Crear_Menu_Eliminar
        Crear_Menu_Eliminar()
        
    def Copia_Seguridad():
        import sqlite3
        import io
        conn = sqlite3.connect("..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\basedatos\\proyinnovatewithproyects.db")  
        with io.open("..\\Proyecto\\Aplicacion\\Copias_De_Seguridad\\backupdatabase_dump.sql", "w") as p: 
            for line in conn.iterdump(): 
                p.write('%s\n' % line)
        conn.close()

        
    Administrar_Admin_Menu = tk.Button(Menu_Admin,text="ADMINISTRAR", font=15, bg= "#f4a020", width=30, command=Open_Admin_Administrar).place(x=450, y=200)
    Actuarizar_Admin_Menu = tk.Button(Menu_Admin,text="ACTUALIZAR USUARIOS", font=15, bg= "#f4a020", width=30, command=Open_Menu_Actualizar).place(x=450, y=300)
    Eliminar_Admin_Menu = tk.Button(Menu_Admin,text="ELIMINAR USUARIOS", font=15, bg= "#f4a020", width=30, command=Open_Menu_Eliminar).place(x=450, y=400)
    Generar_Copia_Seguridad = tk.Button(Menu_Admin, text="GENERAR COPIA DE SEGURIDAD", font=15, bg= "#f4a020", width=30, command=Copia_Seguridad).place(x=450, y=500)
    
    
    
    Menu_Admin.mainloop()
Crear_Menu_Admin()