import tkinter as tk



class VistasNotas:

    def __init__(self):
        #crear ventana principal
        self.root = tk.Tk()
        self.root.title('VistasNotas')
        self.root.geometry('500x600')

        #crear etiquetas
        self.label_title = tk.Label(self.root, text="Notas mode",
                                    font=("arial", 20, "bold"))
        self.label_title.pack()

        self.label_coords = tk.Label(self.root, text="")
        self.label_coords.pack()

        #crear listbox
        self.list_notes = tk.Listbox(self.root)
        self.list_notes.pack()

        #crear entry
        self.new_note = tk.Entry(self.root)
        self.new_note.pack()

        #crear muchos botones
        self.button_insert = tk.Button(self.root, text="Insertar")
        self.button_insert.pack()

        self.button_delete = tk.Button(self.root, text="Eliminar")
        self.button_delete.pack()

        self.button_save = tk.Button(self.root, text="Guardar")
        self.button_save.pack()

        self.button_download_notes= tk.Button(self.root, text="Cargar")
        self.button_download_notes.pack()

        self.button_download = tk.Button(self.root, text="Descargar imagen")
        self.button_download.pack()

        #etiqueta para una imagen
        self.label_image = tk.Label(self.root, text="")
        self.label_image.pack()
