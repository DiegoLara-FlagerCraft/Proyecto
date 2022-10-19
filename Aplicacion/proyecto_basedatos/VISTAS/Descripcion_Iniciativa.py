def Crear_Descripcion_Iniciativas():
    from cProfile import label
    from cgitb import text
    import tkinter as tk
    from tkinter import CENTER, LEFT, ttk
    from tkinter import font
    from turtle import color, left, position
    import tkinter.font as tkFont

    Descripcion_Iniciativas = tk.Tk()
    Descripcion_Iniciativas.config(width=1360, height=768, bg= '#7EADB0')
    Descripcion_Iniciativas.title("INICIATIVAS")
    BienvenidaLabel_Des_Ini = tk.Label(Descripcion_Iniciativas, text="BIENVENIDO A \nINNOVATE WITH \nPROYECTS",font=10,background='#7EADB0',justify=LEFT).place(x=20, y=20)
    FontLabel_Des_Ini = tkFont.Font(size = 20, weight= "bold")
    TextoLabel_Des_Ini = tk.Label(Descripcion_Iniciativas,text="NOMBRE INICIATIVA TECNOLOGICA",font=FontLabel_Des_Ini,background='#7EADB0',justify=CENTER).place(x=500, y=50)

    # INICIATIVAS
    FontText_Des_Ini = tkFont.Font(size = 12, weight= "bold")
    IniciativasCon_Des_Ini = tk.Label(Descripcion_Iniciativas, text="CONTENIDO:", width=120, height=10, justify=LEFT).place(x=300, y=100)
    IniciativasCom_Des_Ini = tk.Label(Descripcion_Iniciativas, text="COMENTARIOS:", width=120, height=10, justify=LEFT).place(x=300, y=300)
    Calificacion_Des_Ini = tk.Label(Descripcion_Iniciativas, text= "CALIFICACION:",font=15,background='#7EADB0').place(x=300, y=510)
    Combox_Calificacion_Des_Ini = ttk.Combobox(Descripcion_Iniciativas, state="readonly", values=[1,2,3,4,5],background='#D9D9D9').place(x=550, y=515)

    # BOTONES

    Siguiente_Des_Ini = tk.Button(text="SIGUIENTE", font=15, bg= "#f4a020", width=20).place(x=400, y=650)
    Volver_Des_Ini = tk.Button(text="VOLVER", font=15, bg= "#f4a020", width=20).place(x=800, y=650)

    Descripcion_Iniciativas.mainloop()
    
Crear_Descripcion_Iniciativas()