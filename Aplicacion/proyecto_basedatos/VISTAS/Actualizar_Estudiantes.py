from multiprocessing.sharedctypes import Value
from tkinter import END
from colorama import Cursor


def Crear_Actualizar_Estudiante():
    from tkinter import ALL
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
    
    Registro_estudiantes = tk.Tk()
    Registro_estudiantes.config(width=1360, height=768, bg= '#7EADB0')
    Registro_estudiantes.title("ACTUALIZAR ESTUDIANTES")
    BienvenidaLabel_Estu = tk.Label(Registro_estudiantes, text="FORMULARIO\nACTUALIZAR\nESTUDIANTES",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Estu = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Estu = tk.Label(Registro_estudiantes,text="ACTUARIZAR ESTUDIANTE\nRELLENE LOS DATOS",font=FontLabel_Estu,background='#7EADB0',justify=CENTER).place(x=450, y=50)


    # FORMULARIO
    
    Correolbl_Estu = tk.Label(Registro_estudiantes, text= "CORREO:",font=15,background='#7EADB0').place(x=300, y=145)
    TexBox_Correo_Estu = tk.Entry(Registro_estudiantes, width=100,background="#D9D9D9")
    TexBox_Correo_Estu.place(x=450, y=150)
    
    TextoMensaje_Estu = tk.Label(Registro_estudiantes,text="DATOS A ACTUALIZAR",font=FontLabel_Estu,background='#7EADB0',justify=CENTER).place(x=450, y=225)

    Nombrelbl_Estu = tk.Label(Registro_estudiantes, text= "NOMBRE:",font=15,background='#7EADB0').place(x=300, y=310)
    TexBox_Nombre_Estu = tk.Entry(Registro_estudiantes, width=100,background="#D9D9D9")
    TexBox_Nombre_Estu.place(x=450, y=315)
    
    Apellidolbl_Estu = tk.Label(Registro_estudiantes, text= "APELLIDO:",font=15,background='#7EADB0').place(x=300, y=355)
    TexBox_Apellido_Estu = tk.Entry(Registro_estudiantes, width=100,background="#D9D9D9")
    TexBox_Apellido_Estu.place(x=450, y=360)

    Fechalbl_Estu = tk.Label(Registro_estudiantes, text= "FECHA DE NACIMIENTO:",font=15,background='#7EADB0').place(x=300, y=410)
    Calendar_Estu = DateEntry(Registro_estudiantes, width=12, background="green", foreground="white", borderwidth=2)
    Calendar_Estu.place(x=550, y=415)

    Semestrelbl_Estu = tk.Label(Registro_estudiantes, text= "SEMESTRE APROBADO:",font=15,background='#7EADB0').place(x=300, y=455)
    Combox_Semestre_Estu = ttk.Combobox(Registro_estudiantes, state="readonly", values=[1,2,3,4,5,6,7,8,9,10],background='#D9D9D9')
    Combox_Semestre_Estu.place(x=550, y=460)

    Facultadlbl_Estu = tk.Label(Registro_estudiantes, text= "FACULTAD:",font=15,background='#7EADB0').place(x=300, y=500)
    Combox_Facultad_Estu = ttk.Combobox(Registro_estudiantes, state="readonly", values=["Administración de Empresas","Administración de Negocios Internacionales","Ciencias Políticas y Gobierno","Comunicación Social - Periodismo","Derecho","Diseño Gráfico","Ingeniería Ambiental","Ingeniería Civil","Ingeniería Electrónica","Ingeniería Eléctrica","Ingeniería Industrial","Ingeniería Mecánica","Ingeniería de Sistemas e Informática","Psicología"], width=40,background='#D9D9D9')
    Combox_Facultad_Estu.place(x=430, y=505)

    Promediolbl_Estu = tk.Label(Registro_estudiantes, text= "PROMEDIO PONDERADO:",font=15,background='#7EADB0').place(x=300, y=545)
    TexBox_Promedio_Estu = tk.Entry(Registro_estudiantes, width=20,background="#D9D9D9")
    TexBox_Promedio_Estu.place(x=560, y=550)
    

    # BOTONES
    def Borrar_Campos():
        TexBox_Nombre_Estu.delete(0, END)
        TexBox_Apellido_Estu.delete(0, END)
        TexBox_Correo_Estu.delete(0, END)
        TexBox_Promedio_Estu.delete(0, END)

    def Actualizar_Estudiante():
        con = lite.connect("..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\basedatos\\proyinnovatewithproyects.db")
        with con:
            cursor = con.cursor()
            def Usuario_Encontrado(correo):
                Buscar_Usuario = ("SELECT es_Correo FROM Estudiantes WHERE Estudiantes.es_Correo = ?")
                cursor.execute(Buscar_Usuario, [(correo)])
                result = cursor.fetchall()
                return result
            
            if Usuario_Encontrado(TexBox_Correo_Estu.get()):
                cursor.execute("UPDATE Estudiantes SET es_Nombre = ?, es_Apellido = ?, es_Fecha_nacimiento = ?, es_Semestre_aprobado = ?, es_Facultad = ?, es_Promedio_ponderado = ?  WHERE Estudiantes.es_Correo = ?", 
                               [(TexBox_Nombre_Estu.get()), (TexBox_Apellido_Estu.get()), (Calendar_Estu.get()), (Combox_Semestre_Estu.get()),
                                (Combox_Facultad_Estu.get()), (TexBox_Promedio_Estu.get()), (TexBox_Correo_Estu.get())])
                messagebox.showinfo("USUARIO", "DATOS ACTUALIZADOS")
                TexBox_Nombre_Estu.delete(0, END)
                TexBox_Apellido_Estu.delete(0, END)
                TexBox_Promedio_Estu.delete(0, END)
                TexBox_Correo_Estu.delete(0, END)
                
            else:
                messagebox.showinfo("USUARIO", "CORREO NO ENCONTRADO")

        cursor.close()
        
        
    Registrarbtn_Estu = tk.Button(Registro_estudiantes,text="ACTUALIZAR", font=15, bg= "#f4a020", command=Actualizar_Estudiante).place(x=500, y=650)
    Borrarbtn_Estu = tk.Button(Registro_estudiantes,text="BORRAR", font=15, bg= "#f4a020", command=Borrar_Campos).place(x=700, y=650)




    Registro_estudiantes.mainloop()

Crear_Actualizar_Estudiante()