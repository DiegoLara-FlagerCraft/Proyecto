import string
from tkinter import Label


def Crear_Eliminar_Iniciativa():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont
    import sqlite3 as lite
    from tkinter import messagebox
    import webbrowser
    import os
    from tkinter import scrolledtext as st

    Eliminar_Iniciativa = tk.Tk()
    Eliminar_Iniciativa.config(width=1360, height=768, bg= '#7EADB0')
    Eliminar_Iniciativa.title("ELIMINAR INICIATIVA")
    BienvenidaLabel_Eliminar_Iniciativa = tk.Label(Eliminar_Iniciativa, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Coordinador_Menu = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Coordinador_Menu = tk.Label(Eliminar_Iniciativa,text="BIENVENIDO COORDINADOR",font=FontLabel_Coordinador_Menu,background='#7EADB0',justify=CENTER).place(x=500, y=50)
    FontLabel_Eliminar_Iniciativa = tkFont.Font(size = 20, weight= "bold")
    
    con = lite.connect("..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\basedatos\\proyinnovatewithproyects.db")
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT ini_Nombre FROM Iniciativa")
        result = cursor.fetchall()
        result = str(result)
        Cambiar = result.replace(" ", "\n")

    # INICIATIVAS
    FontText_Eliminar_Iniciativa = tkFont.Font(size = 15, weight= "bold")
    FontText_Eliminar_Iniciativa2 = tkFont.Font(size = 13)
    Administrar_Eliminar_Iniciativa = tk.Label(Eliminar_Iniciativa, text="ELIMINAR INICIATIVAS TECNOLOGICAS",font=FontText_Eliminar_Iniciativa,background='#7EADB0').place(x=600, y=150)
    Buscar_Eliminar_Iniciativa = tk.Label(Eliminar_Iniciativa, text="BUSCAR INICIATIVA TECNOLOGICA\nPOR MEDIO DEL NOMBRE:",background='#7EADB0', font=FontText_Eliminar_Iniciativa2).place(x=250, y=220)
    TexBox_Buscar_Eliminar_Iniciativa = tk.Entry(Eliminar_Iniciativa, width=100,background="#D9D9D9")
    TexBox_Buscar_Eliminar_Iniciativa.place(x=550, y=230)
    Text_Iniciativas = tk.Label(Eliminar_Iniciativa, text=Cambiar, width=130 , height=15).place(x=250, y=300)
    

    # BOTONES
    def Borrar_Iniciativa():
        con = lite.connect("..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\basedatos\\proyinnovatewithproyects.db")
        with con:
            cursor = con.cursor()
            def Iniciativa_Encontrado(Nombre):
                cursor.execute("SELECT ini_Nombre FROM Iniciativa WHERE Iniciativa.ini_Nombre = ?", [(Nombre)])
                result = cursor.fetchall()
                return result
            if Iniciativa_Encontrado(TexBox_Buscar_Eliminar_Iniciativa.get()):
                cursor.execute("DELETE FROM Iniciativa WHERE ini_Nombre = ?", [TexBox_Buscar_Eliminar_Iniciativa.get()])
                os.remove("..\\Proyecto\\Aplicacion\\archivos_txt_guardados\\"+TexBox_Buscar_Eliminar_Iniciativa.get()+".txt")
                os.remove("..\\Proyecto\\Aplicacion\\archivos_pdf_guardados\\"+TexBox_Buscar_Eliminar_Iniciativa.get()+".pdf")
                os.remove("..\\Proyecto\\Aplicacion\\videosdescargados\\"+TexBox_Buscar_Eliminar_Iniciativa.get()+".mp4")
                messagebox.showinfo("INICIATIVA", "INICIATIVA ELIMINADA")
                TexBox_Buscar_Eliminar_Iniciativa.delete(0, tk.END)
            else:
                messagebox.showinfo("INICIATIVA", "INICIATIVA NO ENCONTRADA")
        cursor.close()
    Buscar_Iniciativa_btn = tk.Button(text="ELIMINAR", font=15, bg= "#f4a020", width=30, command=Borrar_Iniciativa).place(x=500, y=600)
    Eliminar_Iniciativa.mainloop()
    
Crear_Eliminar_Iniciativa()