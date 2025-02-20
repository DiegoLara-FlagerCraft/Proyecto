from fileinput import filename
import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from turtle import width

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
        nombrearchivo = fd.asksaveasfilename(initialdir= "..\\Proyecto\\Aplicacion\\archivos_txt_guardados", title = "Guardar Como", filetypes= (("txt files","*.txt"),("todos los archivos","*,*")))
        if nombrearchivo != '':
            archivo1 = open(nombrearchivo, "w", encoding="utf-8")
            archivo1.write(self.scrolledtext1.get("1.0", tk.END))
            archivo1.close()
            mb.showinfo("INFORMACION", "LOS DATOS FUERON GUARDADOS EN EL ARCHIVO")
            
    
    def abrir(self):
        nombrearchivo = fd.askopenfilename(initialdir= "..\\Proyecto\\Aplicacion\\archivos_txt_guardados", title = "Seleccione el Archivo", filetypes= (("txt files","*.txt"),("todos los archivos","*,*")))
        if nombrearchivo != '':
            archivo1 = open(nombrearchivo, "r", encoding="utf-8")
            contenido = archivo1.read()
            archivo1.close()
            self.scrolledtext1.delete("1.0", tk.END)
            self.scrolledtext1.insert("1.0", contenido)