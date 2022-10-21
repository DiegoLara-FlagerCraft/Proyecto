                    archivotxt = open("..\\Proyecto\\Aplicacion\\archivos_txt_guardados"+TexBox_Buscar_Iniciativa_Tecnologica.get()+".txt", "r", encoding="utf-8")
                    contenino = archivotxt.read()
                    messagebox.showinfo("INFO", contenino)
                    Descripcion_Iniciativa = tk.Label(Iniciativa, text="contenino", width=85, height=20). place(x=50, y=50)