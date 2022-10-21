import string
from tkinter import Label


def Crear_Iniciativa_Tecnologica():
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

    Iniciativa_Tecnologica = tk.Tk()
    Iniciativa_Tecnologica.config(width=1360, height=768, bg= '#7EADB0')
    Iniciativa_Tecnologica.title("INICIATIVAS TECNOLOGICAS")
    BienvenidaLabel_Iniciativa_Tecnologica = tk.Label(Iniciativa_Tecnologica, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Iniciativa_Tecnologica = tkFont.Font(size = 20, weight= "bold")
    
    con = lite.connect("..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\basedatos\\proyinnovatewithproyects.db")
    with con:
        cursor = con.cursor()
        cursor.execute("SELECT ini_Nombre FROM Iniciativa")
        result = cursor.fetchall()
        result = str(result)
        Cambiar = result.replace(" ", "\n")

    # INICIATIVAS
    FontText_Iniciativa_Tecnologica = tkFont.Font(size = 15, weight= "bold")
    FontText_Iniciativa_Tecnologica2 = tkFont.Font(size = 13)
    Administrar_Iniciativa_Tecnologica = tk.Label(Iniciativa_Tecnologica, text="INICIATIVAS TECNOLOGICAS",font=FontText_Iniciativa_Tecnologica,background='#7EADB0').place(x=600, y=150)
    Buscar_Iniciativa_Tecnologica = tk.Label(Iniciativa_Tecnologica, text="BUSCAR INICIATIVA TECNOLOGICA\nPOR MEDIO DEL NOMBRE:",background='#7EADB0', font=FontText_Iniciativa_Tecnologica2).place(x=250, y=220)
    TexBox_Buscar_Iniciativa_Tecnologica = tk.Entry(Iniciativa_Tecnologica, width=100,background="#D9D9D9")
    TexBox_Buscar_Iniciativa_Tecnologica.place(x=550, y=230)
    Text_Iniciativas = tk.Label(Iniciativa_Tecnologica, text=Cambiar, width=130 , height=15).place(x=250, y=300)
    
    

    # BOTONES
    def Buscar_Iniciativa():
        con = lite.connect("..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\basedatos\\proyinnovatewithproyects.db")
        with con:
            cursor = con.cursor()
            def Iniciativa_Encontrado(Nombre):
                cursor.execute("SELECT ini_Nombre FROM Iniciativa WHERE Iniciativa.ini_Nombre = ?", [(Nombre)])
                result = cursor.fetchall()
                return result
            if Iniciativa_Encontrado(TexBox_Buscar_Iniciativa_Tecnologica.get()):
                messagebox.showinfo("INICIATIVA", "INICIATIVA ENCONTRADA")
                
                def Open_Iniciativa():
                    Iniciativa = tk.Tk()
                    Iniciativa.config(width=700, height=700, bg= '#7EADB0')
                    Iniciativa.title(TexBox_Buscar_Iniciativa_Tecnologica.get())
                    
                    archivotxt = open("..\\Proyecto\\Aplicacion\\archivos_txt_guardados\\"+TexBox_Buscar_Iniciativa_Tecnologica.get()+".txt", "r", encoding="utf-8")
                    contenido = archivotxt.read()
                    archivotxt.close()
                    contenido = str(contenido)

                    Titulo_Iniciativa = tk.Label(Iniciativa, text=TexBox_Buscar_Iniciativa_Tecnologica.get(), font=20, background="#7EADB0").place(x=250, y=5)

                    
                    Descripcion_Iniciativa = tk.Label(Iniciativa, text=contenido, width=85, height=20). place(x=50, y=50)
                    # BOTONES
                    
                    def Abrir_PDF():
                        pdf = "..\\Proyecto\\Aplicacion\\archivos_pdf_guardados\\"+TexBox_Buscar_Iniciativa_Tecnologica.get()+".pdf"
                        webbrowser.open_new(pdf)
                    
                    def Abrir_Video():
                        os.system("..\\Proyecto\\Aplicacion\\videosdescargados\\"+TexBox_Buscar_Iniciativa_Tecnologica.get()+".mp4")
                    
                    
                    Abrir_PDF_btn = tk.Button(Iniciativa, text="PDF", font=15, bg= "#f4a020", width=30, command=Abrir_PDF).place(x=180, y=400)
                    Abrir_VIDEO_btn = tk.Button(Iniciativa, text="VIDEO", font=15, bg= "#f4a020", width=30, command=Abrir_Video).place(x=180, y=450)
                    
                    Iniciativa.mainloop()
                Open_Iniciativa()
                
                
            else:
                messagebox.showinfo("INICIATIVA", "INICIATIVA NO ENCONTRADA")
        cursor.close()
    Buscar_Iniciativa_btn = tk.Button(text="BUSCAR", font=15, bg= "#f4a020", width=30, command=Buscar_Iniciativa).place(x=500, y=600)
    Iniciativa_Tecnologica.mainloop()
Crear_Iniciativa_Tecnologica()