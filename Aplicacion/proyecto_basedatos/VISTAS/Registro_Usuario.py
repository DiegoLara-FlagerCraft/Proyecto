from asyncio.windows_events import NULL
from tkinter import END


def Crear_Registro_Usuario():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont
    from tkcalendar import DateEntry
    import sqlite3 as lite
    from tkinter import messagebox
    from tkinter import scrolledtext as st

    Registro_Usuario = tk.Tk()
    Registro_Usuario.config(width=1360, height=768, bg= '#7EADB0')
    Registro_Usuario.title("REGISTRO USUARIOS")
    BienvenidaLabel_Usu = tk.Label(Registro_Usuario, text="FORMULARIO\nREGISTRO\nUSUARIOS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Usu = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Usu = tk.Label(Registro_Usuario,text="REGISTRO USUARIOS\nRELLENE CON SUS DATOS",font=FontLabel_Usu,background='#7EADB0',justify=CENTER).place(x=450, y=50)

    # FORMULARIO
    Nombrelbl_Usu = tk.Label(Registro_Usuario, text= "NOMBRE:",font=15,background='#7EADB0').place(x=300, y=175)
    TexBox_Nombre_Usu = tk.Entry(Registro_Usuario, width=100,background="#D9D9D9")
    TexBox_Nombre_Usu.place(x=450, y=180)

    Apellidolbl_Usu = tk.Label(Registro_Usuario, text= "APELLIDO:",font=15,background='#7EADB0').place(x=300, y=220)
    TexBox_Apellido_Usu = tk.Entry(Registro_Usuario, width=100,background="#D9D9D9")
    TexBox_Apellido_Usu.place(x=450, y=225)

    Correolbl_Usu = tk.Label(Registro_Usuario, text= "CORREO:",font=15,background='#7EADB0').place(x=300, y=265)
    TexBox_Correo_Usu = tk.Entry(Registro_Usuario, width=100,background="#D9D9D9")
    TexBox_Correo_Usu.place(x=450, y=270)

    Fechalbl_Usu = tk.Label(Registro_Usuario, text= "FECHA DE NACIMIENTO:",font=15,background='#7EADB0').place(x=300, y=310)
    Calendar_Usuario = DateEntry(Registro_Usuario, width=12, background="green", foreground="white", borderwidth=2)
    Calendar_Usuario.place(x=550, y=315)

    Contrase_Usu = tk.Label(Registro_Usuario, text= "CONTRASENA:",font=15,background='#7EADB0').place(x=300, y=355)
    Textbox_Contrase_Usu = tk.Entry(Registro_Usuario,background='#D9D9D9', width=100, show="*")
    Textbox_Contrase_Usu.place(x=450, y=360) 
    
    Terminos_Usu = tk.Label(Registro_Usuario, text= "Al registrarse en el aplicativo acepta los terminos y condiciones del mismo", font=10, background='#7EADB0').place(x=300, y=400)



    #BOTONESSS
    def Borrar_Campos():
        TexBox_Nombre_Usu.delete(0, END)
        TexBox_Apellido_Usu.delete(0, END)
        TexBox_Correo_Usu.delete(0, END)
        Textbox_Contrase_Usu.delete(0, END)

    def Registrar_Usuario():
        con = lite.connect("..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\basedatos\\proyinnovatewithproyects.db")
        with con:
            cursor = con.cursor()
        cursor.execute("INSERT INTO Persona (Id_Persona, perso_Nombre, perso_Apellido, perso_Fecha_nacimiento, perso_Correo, perso_Contrase) VALUES (?,?,?,?,?,?)", (None, TexBox_Nombre_Usu.get(), TexBox_Apellido_Usu.get(), Calendar_Usuario.get_date(), TexBox_Correo_Usu.get(), Textbox_Contrase_Usu.get(),))
        con.commit()
        cursor.close()
        TexBox_Nombre_Usu.delete(0, END)
        TexBox_Apellido_Usu.delete(0, END)
        TexBox_Correo_Usu.delete(0, END)
        Textbox_Contrase_Usu.delete(0, END)
        messagebox.showinfo("USUARIO", "USUARIO REGISTRADO EXITOSAMENTE")

    def Volver_Home():
        Registro_Usuario.destroy()
        from HOME import Open_Home
        Open_Home()
        
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

    Registrarbtn_Usu = tk.Button(text="REGISTRARSE", font=15, bg= "#f4a020", command=Registrar_Usuario).place(x=500, y=500)
    Borrarbtn_Usu = tk.Button(text="BORRAR", font=15, bg= "#f4a020", command=Borrar_Campos).place(x=700, y=500)
    Volver_btn = tk.Button(Registro_Usuario, text = "VOLVER", font=20, command=Volver_Home).place(x=1200, y=5)
    Terminos_btn = tk.Button(Registro_Usuario, text = "TERMINOS Y CONDICIONES", font=5, command=Open_Terminos_Condiciones).place(x=510, y=450)


    Registro_Usuario.mainloop()

Crear_Registro_Usuario()