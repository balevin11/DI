from io import BytesIO

import requests
from PIL import Image, ImageTk


def download_image(url, size):
    try:
        #realizar el get de la url y comprobar que fue bien
        response = requests.get(url)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content))
        image.resize((size,size),int("LANCZOS"))
        ImageTk.PhotoImage(image)
        return image

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
        return None