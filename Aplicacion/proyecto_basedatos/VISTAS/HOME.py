from cProfile import label
from dis import show_code
from distutils.cmd import Command
import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import *
from turtle import color
import tkinter.font as tkFont
from tkinter import scrolledtext as st

root = tk.Tk()
root.config(width=1360, height=768)
root.title("BIENVENIDO")
Home = tk.Frame(root)
Home.place(x=0, y=0, width=1360, height=768)
Home.config(bg= '#7EADB0')

#OPEN HOME

def Open_Home():
    def Open_Terminos_Condiciones():
        ventana1 = tk.Tk()
        ventana1.title("TERMINOS Y CONDICIONES")
        scrolledtext1 = st.ScrolledText(ventana1, width=80, height=30)
        scrolledtext1.grid(column = 0, row = 0, padx = 10, pady = 10)
        nombrearchivo = "..\\Proyecto\\Aplicacion\\proyecto_basedatos\\VISTAS\\TERMINOS.txt"
        archivo1 = open(nombrearchivo, "r", encoding="utf-8")
        contenido = archivo1.read()
        archivo1.close()
        scrolledtext1.delete("3.0", tk.END)
        scrolledtext1.insert("1.0", contenido)

    def Open_Contacto():
        ventana2 = tk.Tk()
        ventana2.title("TERMINOS Y CONDICIONES")
        scrolledtext1 = st.ScrolledText(ventana2, width=80, height=30)
        scrolledtext1.grid(column = 0, row = 0, padx = 10, pady = 10)
        nombrearchivo = "..\\Proyecto\\Aplicacion\\proyecto_basedatos\\VISTAS\\CONTACTO.txt"
        archivo1 = open(nombrearchivo, "r", encoding="utf-8")
        contenido = archivo1.read()
        archivo1.close()
        scrolledtext1.delete("3.0", tk.END)
        scrolledtext1.insert("1.0", contenido)
        
        
    buttonRegistrar = tk.Button(Home, text="REGISTRARSE", command=Open_Registro_Roles)
    buttonRegistrar.place(x=1200, y=20)
    buttonIniciar = tk.Button(Home, text="INICIAR SESION", command=Open_Inicio_Roles)
    buttonIniciar.place(x=1090, y=20)
    buttonTerminos = tk.Button(Home, text="TERMINOS Y CONDICIONES", command=Open_Terminos_Condiciones)
    buttonTerminos.place(x=915, y=20)
    buttonContacto = tk.Button(Home, text="CONTACTO" , command= Open_Contacto)
    buttonContacto.place(x=825, y=20)
    labelTitulo = tk.Label(Home, text="BIENVENIDO A INNOVATE WITH PROYECTS",font=10,background='#7EADB0')
    labelTitulo.place(x=20, y=20)
    labelTexto = tk.Label(Home, text="INNOVATE WITH PROYECTS es una aplicacion que te permite como estudiante subir tus iniciativas tecnologicas \n\n"
                        "para que todas aquellas personas interesadas ya sean otros estudiantes, profesores,\n\n" 
                        "empresarios, coordinadores e incluso invitados puedan observar, comentar,\n\n" 
                        "valorar y ponerse en contacto con todas aquellas iniciativas tecnologicas \n\n"
                        "que les llame la atencion \n\n\n"
                        "¡ NO ESPERES MAS !",font=10,background='#7EADB0')

    # CONTENIDO

    def Ingresar_como_Invitado():
        root.destroy()
        from Iniciativa_Tecnologica import Crear_Iniciativa_Tecnologica
        Crear_Iniciativa_Tecnologica()

    labelTexto.place(x=180, y=360)
    Ingresar_Invitado = tk.Button(Home, text="INGRESAR COMO INVITADO", font= "20", bg="#f4a020", command=Ingresar_como_Invitado)
    Ingresar_Invitado.place(x=500, y=690)
    logo = tk.PhotoImage(file= "..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\IMAGENES\\logo.png")
    lbl_img = tk.Label(Home, image = logo)
    lbl_img.place(x=560, y=100)
    root.mainloop()


# REGISTRO ROLES
def Open_Registro_Roles():
    Open_Registro_Roles = tk.Toplevel()
    root.destroy()
        
    # CONTENIDO 

    Registro_roles = tk.Tk()
    Registro_roles.config(width=1360, height=768, bg= '#7EADB0')
    Registro_roles.title("REGISTRO")
    BienvenidaLabel = tk.Label(Registro_roles, text="BIENVENIDO A \nINNOVATE WITH\nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel = tkFont.Font(size = 20, weight= "bold")
    TextoLabel = tk.Label(Registro_roles,text="ELIGA SU TIPO DE USUARIO\nPARA REGISTRARSE EN EL APLICATIVO",font=FontLabel,background='#7EADB0',justify=CENTER).place(x=450, y=100)

    # IMAGENES

    estudiante = tk.PhotoImage(file= "..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\IMAGENES\\estudiante.png")
    lbl_estu = tk.Label(Registro_roles, image = estudiante).place(x=200, y=200)

    admin = tk.PhotoImage(file= "..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\IMAGENES\\Administrador.png")
    lbl_admin = tk.Label(Registro_roles, image = admin).place(x=550, y=200)

    coordinador = tk.PhotoImage(file= "..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\IMAGENES\\coordinador.png")
    lbl_coordinador = tk.Label(Registro_roles, image = coordinador).place(x=900, y=200)

    # BOTONES
    
    def Open_Registro_Estudiante():
        Registro_roles.destroy()
        from Registro_Estudiante import Crear_Registro_Estudiante
        Crear_Registro_Estudiante
        
    def Open_Registro_Usuario():
        Registro_roles.destroy()
        from Registro_Usuario import Crear_Registro_Usuario
        Crear_Registro_Usuario

    def Volver_Home():
        Registro_roles.destroy()
        from HOME import Open_Home
        Open_Home()
        
    Estudiante_btn = tk.Button(Registro_roles, text = "ESTUDIANTE", font=20, command=Open_Registro_Estudiante).place(x=240, y=450)

    Administrador_btn = tk.Button(Registro_roles, text = "ADMINISTRADOR", font=20, command=Open_Registro_Usuario).place(x=575, y=450)

    Coordinador_btn = tk.Button(Registro_roles, text = "COORDINADOR", font=20, command=Open_Registro_Usuario).place(x=930, y=450)
    
    Empresario_btn = tk.Button(Registro_roles, text="EMPRESARIO", font=20, command=Open_Registro_Usuario).place(x=580, y=550)

    Volver_btn = tk.Button(Registro_roles, text = "VOLVER", font=20, command=Volver_Home).place(x=1200, y=5)

    Registro_roles.mainloop()
    
def Open_Inicio_Roles():
    
    Open_Inicio_Roles = tk.Toplevel()
    root.destroy()
    
    Inicio_roles = tk.Tk()
    Inicio_roles.config(width=1360, height=768, bg= '#7EADB0')
    Inicio_roles.title("INICIO DE SESION")
    BienvenidaLabel = tk.Label(Inicio_roles, text="BIENVENIDO A \nINNOVATE WITH\nPROYECTS",font=10,background='#7EADB0',justify=LEFT)
    BienvenidaLabel.place(x=20, y=20)
    FontLabel = tkFont.Font(size = 20, weight= "bold")
    TextoLabel = tk.Label(Inicio_roles,text="ELIGA SU TIPO DE USUARIO\nPARA INGRESAR AL APLICATIVO",font=FontLabel,background='#7EADB0',justify=CENTER)
    TextoLabel.place(x=450, y=100)

    # IMAGENES

    estudiante = tk.PhotoImage(file= "..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\IMAGENES\\estudiante.png")
    lbl_estu = tk.Label(Inicio_roles, image = estudiante)
    lbl_estu.place(x=200, y=200)

    admin = tk.PhotoImage(file= "..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\IMAGENES\\Administrador.png")
    lbl_admin = tk.Label(Inicio_roles, image = admin)
    lbl_admin.place(x=550, y=200)

    coordinador = tk.PhotoImage(file= "..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\IMAGENES\\coordinador.png")
    lbl_coordinador = tk.Label(Inicio_roles, image = coordinador)
    lbl_coordinador.place(x=900, y=200)

    # BOTONES
    
    def Open_Login_Usuarios_Lider():
        Inicio_roles.destroy()
        from Login_Usuarios_Lider import Crear_Login_Usuarios_Lider
        Crear_Login_Usuarios_Lider()

    def Open_Login_Usuarios_Admin():
        Inicio_roles.destroy()
        from Login_Usuarios_Admin import Crear_Login_Usuarios_Admin
        Crear_Login_Usuarios_Admin()

    def Open_Login_Usuarios_Coordinador():
        Inicio_roles.destroy()
        from Login_Usuarios_Coordinador import Crear_Login_Usuarios_Coordinador
        Crear_Login_Usuarios_Coordinador()

    def Open_Login_Empresario():
        Inicio_roles.destroy()
        from Login_Empresario import Crear_Login_Usuarios_Empresario
        Crear_Login_Usuarios_Empresario()

    def Volver_Home():
        Inicio_roles.destroy()
        from HOME import Open_Home
        Open_Home()

    Estudiante_btn = tk.Button(Inicio_roles, text = "ESTUDIANTE", font=20, command=Open_Login_Usuarios_Lider)
    Estudiante_btn.place(x=240, y=450)

    Administrador_btn = tk.Button(Inicio_roles, text = "ADMINISTRADOR", font=20, command=Open_Login_Usuarios_Admin)
    Administrador_btn.place(x=575, y=450)

    Coordinador_btn = tk.Button(Inicio_roles, text = "COORDINADOR", font=20, command=Open_Login_Usuarios_Coordinador)
    Coordinador_btn.place(x=930, y=450)
    
    Empresario_btn = tk.Button(Inicio_roles, text="EMPRESARIO", font=20, command=Open_Login_Empresario).place(x=580, y=550)

    Volver_btn = tk.Button(Inicio_roles, text = "VOLVER", font=20, command=Volver_Home).place(x=1200, y=5)
    Inicio_roles.mainloop()
        
Open_Home()