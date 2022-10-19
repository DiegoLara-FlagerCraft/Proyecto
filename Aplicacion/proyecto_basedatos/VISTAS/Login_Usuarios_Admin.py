from multiprocessing.sharedctypes import Value
from pickle import TRUE
from tkinter import messagebox

def Crear_Login_Usuarios_Admin():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont
    import sqlite3 as lite

    Login_Usuario_Admin = tk.Tk()
    Login_Usuario_Admin.config(width=1360, height=768, bg= '#7EADB0')
    Login_Usuario_Admin.title("INICIAR SESION")
    BienvenidaLabel_Log = tk.Label(Login_Usuario_Admin, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Log = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Log = tk.Label(Login_Usuario_Admin,text="LOGIN USUARIO\nINGRESE SUS DATOS",font=FontLabel_Log,background='#7EADB0',justify=CENTER).place(x=550, y=50)

    # INICIO

    Email_Log = tk.Label(Login_Usuario_Admin, text= "EMAIL:",font=15,background='#7EADB0').place(x=300, y=175)
    TexBox_Email_Log = tk.Entry(Login_Usuario_Admin, width=100,background="#D9D9D9")
    TexBox_Email_Log.place(x=475, y=180)

    Contraseña_Log = tk.Label(Login_Usuario_Admin, text= "CONTRASEÑA:",font=15,background='#7EADB0').place(x=300, y=220)
    TexBox_Contrasena_Log = tk.Entry(Login_Usuario_Admin, width=100,background="#D9D9D9")
    TexBox_Contrasena_Log.place(x=475, y=225)
    
    # BOTON

    def Iniciar_sesion():
        con = lite.connect("C:\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\basedatos\\proyinnovatewithproyects.db")
        with con:
            cursor = con.cursor()
            Buscar_Usuario = ("SELECT perso_Correo, perso_Contrase FROM Persona WHERE Persona.perso_Correo = ? AND Persona.perso_Contrase = ?")
            cursor.execute(Buscar_Usuario, [(TexBox_Email_Log.get()), (TexBox_Contrasena_Log.get())])

            def Usuario_Encontrado(correo, contraseña):
                Buscar_Usuario = ("SELECT perso_Correo, perso_Contrase FROM Persona WHERE Persona.perso_Correo = ? AND Persona.perso_Contrase = ?")
                cursor.execute(Buscar_Usuario, [(correo), (contraseña)])
                result = cursor.fetchall()
                return result
            
            if Usuario_Encontrado(TexBox_Email_Log.get(), TexBox_Contrasena_Log.get()):
                Login_Usuario_Admin.destroy()
                from Administrador_Administrar import Crear_Admin_Administrar
                Crear_Admin_Administrar()

        cursor.close()
       
    Iniciar_Log_Admin = tk.Button(Login_Usuario_Admin,text="INICIAR SESION", font=15, bg= "#f4a020", command=Iniciar_sesion).place(x=600, y=400)

    # IMAGENES

    logo = tk.PhotoImage(file= "C:\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\IMAGENES\\logo.png")
    lbl_img = tk.Label(Login_Usuario_Admin, image = logo).place(x=555, y=500)

    Crear_Login_Usuarios_Admin.mainloop()