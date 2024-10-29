from tkinter import mainloop

import VistasNotas
import NotasModel
import ControladorNotas


if __name__ == '__main__':
    #inicializar todas nuestras clases
    model = NotasModel.NotasModel()
    vista = VistasNotas.VistasNotas()
    controlador = ControladorNotas.ControladorNotas(model, vista)

    mainloop()

