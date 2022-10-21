from email import message
from tkinter import messagebox


def Crear_Eliminar_Usuarios():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont
    import sqlite3 as lite

    Eliminar_Usuarios = tk.Tk()
    Eliminar_Usuarios.config(width=1360, height=768, bg= '#7EADB0')
    Eliminar_Usuarios.title("ELIMINAR USUARIOS")
    BienvenidaLabel_Admin_Admi = tk.Label(Eliminar_Usuarios, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Admin_Admi = tkFont.Font(size = 20, weight= "bold")

    # INICIATIVAS
    FontText_Admin_Admi = tkFont.Font(size = 15, weight= "bold")
    FontText_Admin_Admi2 = tkFont.Font(size = 13)
    Administrar_Admin_Admi = tk.Label(Eliminar_Usuarios, text="ELIMINAR USUARIO:",font=FontText_Admin_Admi,background='#7EADB0').place(x=300, y=150)
    Buscar_Admin_Admi = tk.Label(Eliminar_Usuarios, text="ELIMINAR USUARIO\nPOR MEDIO DE EL CORREO:",background='#7EADB0', font=FontText_Admin_Admi2).place(x=300, y=220)
    TexBox_Buscar_Admin_Admi = tk.Entry(Eliminar_Usuarios, width=100,background="#D9D9D9")
    TexBox_Buscar_Admin_Admi.place(x=550, y=230)

    # BOTONES
    
    def Eliminar_Usuario():
        con = lite.connect("..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\basedatos\\proyinnovatewithproyects.db")
        with con:
            cursor = con.cursor()
            def Usuario_Encontrado(Correo):
                cursor.execute("SELECT perso_Correo FROM Persona WHERE Persona.perso_Correo = ?", [(Correo)])
                result = cursor.fetchall()
                return result
            if Usuario_Encontrado(TexBox_Buscar_Admin_Admi.get()):
                cursor.execute("DELETE FROM Persona WHERE perso_Correo = ?", [TexBox_Buscar_Admin_Admi.get()])
                messagebox.showinfo("USUARIO", "USUARIO ELIMINADO")
                TexBox_Buscar_Admin_Admi.delete(0, tk.END)
            else:
                messagebox.showinfo("USUARIO", "CORREO NO ENCONTRADO")
        cursor.close()

    Eliminar_Usuario_btn = tk.Button(text="ELIMINAR", font=15, bg= "#f4a020", width=30, command=Eliminar_Usuario).place(x=500, y=300)
    Eliminar_Usuarios.mainloop()