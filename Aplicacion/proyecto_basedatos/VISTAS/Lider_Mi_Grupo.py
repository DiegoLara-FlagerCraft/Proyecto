from tkinter import *
def Crear_Lider_Mi_Grupo():
    from cProfile import label
    from cgitb import text
    from optparse import Values
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont

    Lider_Mi_Grupo = tk.Tk()
    Lider_Mi_Grupo.config(width=1360, height=768, bg= '#7EADB0')
    Lider_Mi_Grupo.title("ESTUDIANTE LIDER - MI GRUPO")
    BienvenidaLabel_Lider_Mi_Grupo = tk.Label(Lider_Mi_Grupo, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Lider_Mi_Grupo = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Lider_Mi_Grupo = tk.Label(Lider_Mi_Grupo,text="BIENVENIDO LIDER",font=FontLabel_Lider_Mi_Grupo,background='#7EADB0',justify=CENTER).place(x=500, y=50)

    # INICIATIVAS
    FontText_Lider_Mi_Grupo = tkFont.Font(size = 15, weight= "bold")
    Administrar_Lider_Mi_Grupo = tk.Label(Lider_Mi_Grupo, text="ESTUDIANTES REGISTRADOS \nPARA ESTA INICIATIVA:",font=FontText_Lider_Mi_Grupo,background='#7EADB0', justify="left").place(x=300, y=150)

    #LIST BOX
    Estudiantes_Lider_Mi_Grupo = Listbox(Lider_Mi_Grupo, width=100, bg="#D9D9D9")
    Estudiantes_Lider_Mi_Grupo.pack()
    Estudiantes_Lider_Mi_Grupo.insert(0,"ESTUDIANTE #1", "ESTUDIANTE #2")
    Estudiantes_Lider_Mi_Grupo.place(x=300, y=250)
    # BOTONES

    def Volver_Menu_Lider():
        Lider_Mi_Grupo.destroy()
        from Menu_Estudiante_Lider import Crear_Menu_Estudiante_Lider
        Crear_Menu_Estudiante_Lider()

    Confirmar_Lider_Mi_Grupo = tk.Button(text="CONFIRMAR", font=15, bg= "#f4a020", width=20).place(x=200, y=600)
    Editar_Lider_Mi_Grupo = tk.Button(text="EDITAR", font=15, bg= "#f4a020", width=20).place(x=500, y=600)
    Menu_Lider_Mi_Grupo = tk.Button(text="VOLVER AL MENU", font=15, bg= "#f4a020", width=20).place(x=800, y=600)
    Volver_Lider_Grupo = tk.Button(text="VOLVER", font=15, bg= "#f4a020", width=20, command=Volver_Menu_Lider).place(x=500, y=650)
    
    Lider_Mi_Grupo.mainloop()