from msilib.schema import Directory
from tkinter import *
def Crear_Lider_Mi_Proyecto():
    from cProfile import label
    from cgitb import text
    from optparse import Values
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont
    from tkinter import filedialog as fd
    from pytube import YouTube
    from tkinter import messagebox as Messagebox
    from tkPDFViewer import tkPDFViewer as pdf
    import sqlite3 as lite
    from tkinter import messagebox
    from fileinput import filename
    import tkinter as tk
    from tkinter import scrolledtext as st
    import sys
    from tkinter import messagebox as mb
    from turtle import width
    import shutil
    import webbrowser
        

    Lider_Mi_Proyecto = tk.Tk()
    Lider_Mi_Proyecto.config(width=1360, height=768, bg= '#7EADB0')
    Lider_Mi_Proyecto.title("ESTUDIANTE LIDER - MI GRUPO")
    BienvenidaLabel_Lider_Mi_Proyecto = tk.Label(Lider_Mi_Proyecto, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Lider_Mi_Proyecto = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Lider_Mi_Proyecto = tk.Label(Lider_Mi_Proyecto,text="BIENVENIDO LIDER",font=FontLabel_Lider_Mi_Proyecto,background='#7EADB0',justify=CENTER).place(x=500, y=50)

    # TEXTO
    FontText_Lider_Mi_Proyecto = tkFont.Font(size = 15, weight= "bold")
    Texto_Lider_Mi_Proyecto = tk.Label(Lider_Mi_Proyecto, text="Subir los archivos solicitados para publicar la Iniciativa Tecnologica:",font=FontText_Lider_Mi_Proyecto,background='#7EADB0', justify="left").place(x=300, y=100)

    Titulo_Lider_Mi_Proyecto = tk.Label(Lider_Mi_Proyecto, text= "TITULO PROYECTO:",font=15,background='#7EADB0')
    Titulo_Lider_Mi_Proyecto.place(x=300, y=175)
    TexBox_Titulo_Lider_Mi_Proyecto = tk.Entry(Lider_Mi_Proyecto, width=100,background="#D9D9D9")
    TexBox_Titulo_Lider_Mi_Proyecto.place(x=525, y=180)

    def Subir_Txt():
        class Aplicacion:
            def __init__(self):
                self.ventana1 = tk.Tk()
                self.agregar_menu()
                self.scrolledtext1 = st.ScrolledText(self.ventana1, width=80, height=20)
                self.scrolledtext1.grid(column = 0, row = 0, padx = 10, pady = 10)
                self.ventana1.mainloop()

            def agregar_menu(self):
                menubar1 = tk.Menu(self.ventana1)
                self.ventana1.config(menu=menubar1)
                opciones1 = tk.Menu(menubar1, tearoff=0)
                opciones1.add_command(label="Guardar Archivo", command=self.guardar)
                opciones1.add_command(label="Abrir Archivo", command=self.abrir)
                opciones1.add_separator()
                opciones1.add_command(label="Salir", command=self.salir)
                menubar1.add_cascade(label="Archivo", menu=opciones1)

            def salir(self):
                sys.exit(0)

            def guardar(self):
                nombrearchivo = "..\\Proyecto\\Aplicacion\\archivos_txt_guardados\\"+TexBox_Titulo_Lider_Mi_Proyecto.get()+".txt"
                if nombrearchivo != '':
                    archivo1 = open(nombrearchivo, "w", encoding="utf-8")
                    archivo1.write(self.scrolledtext1.get("1.0", tk.END))
                    archivo1.close()
                    self.ventana1.destroy()
                    mb.showinfo("INFORMACION", "LOS DATOS FUERON GUARDADOS EN EL ARCHIVO")
                    
            
            def abrir(self):
                nombrearchivo = fd.askopenfilename(initialdir= "..\\Proyecto\\Aplicacion\\archivos_txt_guardados", title = "Seleccione el Archivo", filetypes= (("txt files","*.txt"),("todos los archivos","*,*")))
                if nombrearchivo != '':
                    archivo1 = open(nombrearchivo, "r", encoding="utf-8")
                    contenido = archivo1.read()
                    archivo1.close()
                    self.scrolledtext1.delete("1.0", tk.END)
                    self.scrolledtext1.insert("1.0", contenido)
                    self.ventana1.destroy()
                    
        aplicacion = Aplicacion()

    Txt_Lider_Mi_Proyecto = tk.Label(Lider_Mi_Proyecto, text= "SUBIR ARCHIVO .TXT:",font=15,background='#7EADB0').place(x=300, y=220)
    Insertar_Archivo_Txt = Button(Lider_Mi_Proyecto, text= "SUBIR ARCHIVO TXT", command=Subir_Txt)
    Insertar_Archivo_Txt.place(x=525, y=220)

    def Subir_PDF():
        nombrearchivo = fd.askopenfilename(initialdir= "C:\\Documentos", title = "Seleccione el Archivo", filetypes= (("txt files","*.pdf"),("todos los archivos","*,*")))
        shutil.copy2(nombrearchivo, "..\\Proyecto\\Aplicacion\\archivos_pdf_guardados\\"+TexBox_Titulo_Lider_Mi_Proyecto.get()+".pdf")

    Ppt_Lider_Mi_Proyecto = tk.Label(Lider_Mi_Proyecto, text= "SUBIR ARCHIVO .PDF:",font=15,background='#7EADB0').place(x=300, y=265)
    Insertar_Archivo_Ppt = Button(Lider_Mi_Proyecto, text= "SUBIR ARCHIVO PDF", command=Subir_PDF)
    Insertar_Archivo_Ppt.place(x=525, y=265)


    Video_Lider_Mi_Proyecto = tk.Label(Lider_Mi_Proyecto, text= "SUBIR ARCHIVO .MP4:",font=15,background='#7EADB0').place(x=300, y=310)
    Insertar_Video = tk.Entry(Lider_Mi_Proyecto, width=100,background="#D9D9D9")
    Insertar_Video.place(x=525, y=315)
    
    def Descargar_Video_py():
        Enlace = Insertar_Video.get()
        Video = YouTube(Enlace)
        Descarga = Video.streams.get_lowest_resolution()
        Descarga.download("..\\Proyecto\\Aplicacion\\videosdescargados")
        
    Descargar_Video = Button(Lider_Mi_Proyecto, text= "DESCARGAR", command=Descargar_Video_py)
    Descargar_Video.place(x=1150, y=312)
    


    # BOTONES

    def Volver_Menu_Lider():
        Lider_Mi_Proyecto.destroy()
        from Menu_Estudiante_Lider import Crear_Menu_Estudiante_Lider
        Crear_Menu_Estudiante_Lider()
        
    def Subir_Iniciativa():
        con = lite.connect("..\\Proyecto\\Aplicacion\\proyecto_basedatos\\src\\basedatos\\proyinnovatewithproyects.db")
        with con:
            cursor = con.cursor()
        cursor.execute("INSERT INTO Iniciativa (Id_Iniciativa, ini_Nombre) VALUES (?,?)", (None, TexBox_Titulo_Lider_Mi_Proyecto.get()))
        con.commit()
        cursor.close()
        nombrearchivo = fd.askopenfilename(initialdir= "..\\Proyecto\\Aplicacion\\videosdescargados", title = "Seleccione el Archivo", filetypes= (("txt files","*.mp4"),("todos los archivos","*,*")))
        shutil.move(nombrearchivo, "..\\Proyecto\\Aplicacion\\videosdescargados\\"+TexBox_Titulo_Lider_Mi_Proyecto.get()+".mp4")
        TexBox_Titulo_Lider_Mi_Proyecto.delete(0, END)
        messagebox.showinfo("INICIATIVA", "INICIATIVA REGISTRADA")
        
        

    Editar_Lider_Mi_Proyecto = tk.Button(text="SUBIR INICIATIVA TECNOLOGICA", font=15, bg= "#f4a020", width=30, command=Subir_Iniciativa).place(x=450, y=600)
    Volver_Lider_Grupo = tk.Button(text="VOLVER", font=15, bg= "#f4a020", width=20, command=Volver_Menu_Lider).place(x=500, y=650)

    Lider_Mi_Proyecto.mainloop()
Crear_Lider_Mi_Proyecto()
