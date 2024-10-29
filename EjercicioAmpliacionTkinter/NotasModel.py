


class NotasModel:
    def __init__(self):
        #incializar el array para guardar notas
        self.notas = []

    #añadir nueva nota al array
    def agregar_nota(self, new_note):
        self.notas.append(new_note)


    #eliminar nota del array
    def eliminar_nota(self, i):
        del self.notas[i]

    #devolver las notas del array
    def obtener_notas(self):
        return self.notas

    #abrir fichero txt y grabar notas array
    def guardar_notas(self):
        archive = open('notas.txt', 'w')
        for nota in self.notas:
            archive.write(str(nota) + '\n')
        archive.close()

    #abrir fichero txt y grabar su contenido
    def cargar_notas(self):
        try:
            with open("notas.txt", "r") as archivo:
                self.notas = [linea.strip() for linea in archivo]
        except FileNotFoundError:
            self.notas = []
