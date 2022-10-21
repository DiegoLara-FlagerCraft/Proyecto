def Crear_Eliminar_Estudiantes():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont
    import sqlite3 as lite
    from tkinter import messagebox

    Eliminar_Estudiantes = tk.Tk()
    Eliminar_Estudiantes.config(width=1360, height=768, bg= '#7EADB0')
    Eliminar_Estudiantes.title("ELIMINAR ESTUDIANTES")
    BienvenidaLabel_Admin_Admi = tk.Label(Eliminar_Estudiantes, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Admin_Admi = tkFont.Font(size = 20, weight= "bold")

    # INICIATIVAS
    FontText_Admin_Admi = tkFont.Font(size = 15, weight= "bold")
    FontText_Admin_Admi2 = tkFont.Font(size = 13)
    Administrar_Admin_Admi = tk.Label(Eliminar_Estudiantes, text="ELIMINAR ESTUDIANTES:",font=FontText_Admin_Admi,background='#7EADB0').place(x=300, y=150)
    Buscar_Admin_Admi = tk.Label(Eliminar_Estudiantes, text="ELIMINAR USUARIO\nPOR MEDIO DE EL CORREO:",background='#7EADB0', font=FontText_Admin_Admi2).place(x=300, y=220)
    TexBox_Buscar_Admin_Admi = tk.Entry(Eliminar_Estudiantes, width=100,background="#D9D9D9")
    TexBox_Buscar_Admin_Admi.place(x=550, y=230)

    # BOTONES
    def Eliminar_Estudiante():
        con = lite.connect("..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\basedatos\\proyinnovatewithproyects.db")
        with con:
            cursor = con.cursor()
            def Usuario_Encontrado(Correo):
                cursor.execute("SELECT es_Correo FROM Estudiantes WHERE Estudiantes.es_Correo = ?", [(Correo)])
                result = cursor.fetchall()
                return result
            if Usuario_Encontrado(TexBox_Buscar_Admin_Admi.get()):
                cursor.execute("DELETE FROM Estudiantes WHERE es_Correo = ?", [TexBox_Buscar_Admin_Admi.get()])
                messagebox.showinfo("USUARIO", "USUARIO ELIMINADO")
                TexBox_Buscar_Admin_Admi.delete(0, tk.END)
            else:
                messagebox.showinfo("USUARIO", "CORREO NO ENCONTRADO")
        cursor.close()
    Eliminar_Usuario_btn = tk.Button(text="ELIMINAR", font=15, bg= "#f4a020", width=30, command=Eliminar_Estudiante).place(x=500, y=300)
    Eliminar_Estudiantes.mainloop()