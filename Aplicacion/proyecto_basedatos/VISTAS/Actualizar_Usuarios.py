from asyncio.windows_events import NULL
from tkinter import END


def Crear_Actualizar_Usuario():
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
    Registro_Usuario.title("ACTUALIZAR USUARIOS")
    BienvenidaLabel_Usu = tk.Label(Registro_Usuario, text="FORMULARIO\nACTUALIZAR\nUSUARIOS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Usu = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Usu = tk.Label(Registro_Usuario,text="ACTUALIZAR USUARIOS\nRELLENE LOS DATOS",font=FontLabel_Usu,background='#7EADB0',justify=CENTER).place(x=450, y=50)

    # FORMULARIO
    Correolbl_Usu = tk.Label(Registro_Usuario, text= "CORREO USUARIO:",font=15,background='#7EADB0').place(x=300, y=150)
    TexBox_Correo_Usu = tk.Entry(Registro_Usuario, width=100,background="#D9D9D9")
    TexBox_Correo_Usu.place(x=500, y=155)
    
    TextoMensaje_Usu = tk.Label(Registro_Usuario,text="DATOS A ACTUALIZAR",font=FontLabel_Usu,background='#7EADB0',justify=CENTER).place(x=450, y=200)
    
    Nombrelbl_Usu = tk.Label(Registro_Usuario, text= "NOMBRE:",font=15,background='#7EADB0').place(x=300, y=280)
    TexBox_Nombre_Usu = tk.Entry(Registro_Usuario, width=100,background="#D9D9D9")
    TexBox_Nombre_Usu.place(x=450, y=280)

    Apellidolbl_Usu = tk.Label(Registro_Usuario, text= "APELLIDO:",font=15,background='#7EADB0').place(x=300, y=325)
    TexBox_Apellido_Usu = tk.Entry(Registro_Usuario, width=100,background="#D9D9D9")
    TexBox_Apellido_Usu.place(x=450, y=325)

    Fechalbl_Usu = tk.Label(Registro_Usuario, text= "FECHA DE NACIMIENTO:",font=15,background='#7EADB0').place(x=300, y=370)
    Calendar_Usuario = DateEntry(Registro_Usuario, width=12, background="green", foreground="white", borderwidth=2)
    Calendar_Usuario.place(x=550, y=370)
    



    #BOTONESSS
    def Borrar_Campos():
        TexBox_Nombre_Usu.delete(0, END)
        TexBox_Apellido_Usu.delete(0, END)
        TexBox_Correo_Usu.delete(0, END)

    def Actualizar_Usuario():
        con = lite.connect("..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\basedatos\\proyinnovatewithproyects.db")
        with con:
            cursor = con.cursor()
            def Usuario_Encontrado(correo):
                Buscar_Usuario = ("SELECT perso_Correo FROM Persona WHERE Persona.perso_Correo = ?")
                cursor.execute(Buscar_Usuario, [(correo)])
                result = cursor.fetchall()
                return result
            
            if Usuario_Encontrado(TexBox_Correo_Usu.get()):
                cursor.execute("UPDATE Persona SET perso_Nombre = ?, perso_Apellido = ?, perso_Fecha_nacimiento = ?  WHERE Persona.perso_Correo = ?", 
                               [(TexBox_Nombre_Usu.get()), (TexBox_Apellido_Usu.get()), (Calendar_Usuario.get()), (TexBox_Correo_Usu.get())])
                messagebox.showinfo("USUARIO", "DATOS ACTUALIZADOS")
                TexBox_Nombre_Usu.delete(0, END)
                TexBox_Apellido_Usu.delete(0, END)
                TexBox_Correo_Usu.delete(0, END)
            else:
                messagebox.showinfo("USUARIO", "CORREO NO ENCONTRADO")

        cursor.close()

    Registrarbtn_Usu = tk.Button(text="ACTUALIZAR", font=15, bg= "#f4a020", command=Actualizar_Usuario).place(x=500, y=450)
    Borrarbtn_Usu = tk.Button(text="BORRAR", font=15, bg= "#f4a020", command=Borrar_Campos).place(x=700, y=450)

    Registro_Usuario.mainloop()