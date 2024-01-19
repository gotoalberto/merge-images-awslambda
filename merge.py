import os
import urllib.parse
from io import BytesIO
from PIL import Image, ImageDraw
import requests

def lambda_handler(event, context):
    try:
        # Obtén las URL de las imágenes desde los parámetros de la solicitud
        img1_url = event['queryStringParameters']['img1']
        img2_url = event['queryStringParameters']['img2']

        # Descarga las imágenes desde las URL proporcionadas
        img1 = Image.open(BytesIO(requests.get(urllib.parse.unquote(img1_url)).content))
        img2 = Image.open(BytesIO(requests.get(urllib.parse.unquote(img2_url)).content))

        # Asegúrate de que ambas imágenes tengan el mismo tamaño
        img2 = img2.resize(img1.size)

        # Mezcla las imágenes superponiendo una sobre la otra
        result_img = Image.alpha_composite(img1.convert("RGBA"), img2.convert("RGBA"))

        # Crea un objeto BytesIO para almacenar la imagen resultante
        result_img_bytes = BytesIO()
        result_img.save(result_img_bytes, format="PNG")
        result_img_bytes.seek(0)

        # Devuelve la imagen resultante como respuesta
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'image/png'},
            'body': result_img_bytes.read().decode('base64')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }