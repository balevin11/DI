from io import BytesIO
import requests
from PIL import Image
from PIL.Image import Resampling


#descargar imagen
def download_image(url, size):
    try:
        #realizar el get de la url y comprobar que fue bien
        response = requests.get(url)
        response.raise_for_status()

        #abrir imagen y redimensionarla con alta calidad
        image = Image.open(BytesIO(response.content))
        image = image.resize((size,size),Resampling.LANCZOS)

        return image
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
        return None
