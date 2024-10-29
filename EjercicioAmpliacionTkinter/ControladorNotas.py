import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading
from tkinter import messagebox


class ControladorNotas:
    #recibir la vista y el modelo y inicializarlos
    def __init__(self, model, vista):
        self.vista = vista
        self.model = model

        #asociar los comandos a sus respectivos botones
        vista.button_insert.config(command=self.agregar_nota)
        vista.button_delete.config(command=self.eliminar_nota)
        vista.button_save.config(command=self.guardar_notas)
        vista.button_download_notes.config(command=self.cargar_notas)
        vista.button_download.config(command=self.descargar_imagen)

        #crear el bind
        vista.root.bind("<Button-1>", self.actualizar_coordenadas)

        #cargar las notas de la base de notas.txt y mostrarlo
        model.cargar_notas()
        self.actualizar_listbox()

    #añadir nota en la listbox
    def agregar_nota(self):
        self.model.agregar_nota(self.vista.new_note.get())
        self.actualizar_listbox()

    #eliminar nota de la listbox
    def eliminar_nota(self):
        i = self.vista.list_notes.curselection()
        for j in i:
            self.model.eliminar_nota(j)
        self.actualizar_listbox()

    #guardar las notas en notas.txt
    def guardar_notas(self):
        self.model.guardar_notas()
        messagebox.showinfo("Guardado", "El guardado "
                            "se realizó correctamente")

    #rescatar las notas de notas.txt a la listbox
    def cargar_notas(self):
        self.model.cargar_notas()
        self.actualizar_listbox()

    #crear un hilo y llamar descargar imagen
    def descargar_imagen(self):
        url = ('https://raw.githubusercontent.com/balevin11/DI/'
               'main/EjercicioAmpliacionTkinter/imagen.jpg')
        hilo = threading.Thread(target=self.descargar_imagen_hilo,
                                args=(url,))
        hilo.start()

    #descargar y mostrar una imagen
    def descargar_imagen_hilo(self, url):
        try:
            #obtener la imagen
            respuesta = requests.get(url)
            respuesta.raise_for_status()

            #cargar la imagen en una variable
            imagen = Image.open(BytesIO(respuesta.content))
            imagen_tk = ImageTk.PhotoImage(imagen)

            # Actualizar la interfaz en el hilo principal
            self.vista.label_image.config(image=imagen_tk)
            self.vista.label_image.image = imagen_tk
        except requests.exceptions.RequestException as e:
            print(f"Error al descargar la imagen: {e}")
            self.vista.label_image.config(text="Error al descargar "
                                               "la imagen.")

    #mostrar coordenadas del último clic
    def actualizar_coordenadas(self,event):
        coords = [event.x, event.y]
        self.vista.label_coords.config(text=coords)

    #cargar las notas guardadas en el model
    def actualizar_listbox(self):
        self.vista.list_notes.delete(0,tk.END)
        notas = self.model.obtener_notas()
        for nota in notas:
            self.vista.list_notes.insert(tk.END, nota)
