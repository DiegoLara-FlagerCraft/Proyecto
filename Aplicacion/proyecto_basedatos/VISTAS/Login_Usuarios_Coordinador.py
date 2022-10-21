from multiprocessing.sharedctypes import Value
from pickle import TRUE
from tkinter import messagebox

def Crear_Login_Usuarios_Coordinador():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont
    import sqlite3 as lite
    from tkinter import messagebox

    Login_Usuario_Coordinador = tk.Tk()
    Login_Usuario_Coordinador.config(width=1360, height=768, bg= '#7EADB0')
    Login_Usuario_Coordinador.title("INICIAR SESION")
    BienvenidaLabel_Log = tk.Label(Login_Usuario_Coordinador, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Log = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Log = tk.Label(Login_Usuario_Coordinador,text="LOGIN USUARIO\nINGRESE SUS DATOS",font=FontLabel_Log,background='#7EADB0',justify=CENTER).place(x=550, y=50)

    # INICIO

    Email_Log = tk.Label(Login_Usuario_Coordinador, text= "EMAIL:",font=15,background='#7EADB0').place(x=300, y=175)
    TexBox_Email_Log = tk.Entry(Login_Usuario_Coordinador, width=100,background="#D9D9D9")
    TexBox_Email_Log.place(x=475, y=180)

    Contraseña_Log = tk.Label(Login_Usuario_Coordinador, text= "CONTRASEÑA:",font=15,background='#7EADB0').place(x=300, y=220)
    TexBox_Contrasena_Log = tk.Entry(Login_Usuario_Coordinador, width=100,background="#D9D9D9", show="*")
    TexBox_Contrasena_Log.place(x=475, y=225)
    
    # BOTON

    def Iniciar_sesion():
        con = lite.connect("..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\basedatos\\proyinnovatewithproyects.db")
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
                Login_Usuario_Coordinador.destroy()
                from Menu_Coordinador import Crear_Menu_Coordinador
                Crear_Menu_Coordinador()
            else:
                messagebox.showinfo("USUARIO", "EL CORREO O LA CONTRASEÑA NO SON VALIDOS")

        cursor.close()

    def Volver_Home():
        Login_Usuario_Coordinador.destroy()
        from HOME import Open_Home
        Open_Home()
       
    Iniciar_Log_Coordinador = tk.Button(Login_Usuario_Coordinador,text="INICIAR SESION", font=15, bg= "#f4a020", command=Iniciar_sesion).place(x=600, y=400)
    Volver_btn = tk.Button(Login_Usuario_Coordinador, text = "VOLVER", font=20, command=Volver_Home).place(x=1200, y=5)

    # IMAGENES

    logo = tk.PhotoImage(file= "..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\IMAGENES\\logo.png")
    lbl_img = tk.Label(Login_Usuario_Coordinador, image = logo).place(x=555, y=500)

    Crear_Login_Usuarios_Coordinador.mainloop()