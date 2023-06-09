from PIL import Image
import os

# Ruta de la carpeta padre
directorio_padre = 'app/testeddata_creator/'

# Rutas de los directorios
directorio_fotos = os.path.join(directorio_padre, 'fotos')
directorio_image = os.path.join(directorio_padre, 'images')
directorio_gt = os.path.join(directorio_padre, 'gt')

# Crear directorio "images"
os.makedirs(directorio_image, exist_ok=True)

# Crear directorio "gt"
os.makedirs(directorio_gt, exist_ok=True)

# Enumerar y procesar las fotos
contador = 1

for archivo in os.listdir(directorio_fotos):
    if archivo.lower().endswith(('.jpg', '.png', '.gif', 'bmp')):
        # Ruta de la foto original
        ruta_foto = os.path.join(directorio_fotos, archivo)

        # Ruta de la foto en escala de grises y formato TIFF
        ruta_foto_gris = os.path.join(directorio_image, f"{contador}.tiff")

        # Ruta del archivo de texto
        ruta_archivo_texto = os.path.join(directorio_gt, f"{contador}.gt.txt")

        # Convertir la foto a escala de grises y formato TIFF
        imagen = Image.open(ruta_foto)
        imagen_gris = imagen.convert("L")
        imagen_gris.save(ruta_foto_gris, "TIFF")

        # Crear el archivo de texto
        with open(ruta_archivo_texto, 'w') as archivo_texto:
            # Los datos de la variable 'contenido' se cargaron manualmente, pero en un futuro se buscará
            # que los mismos provengan desde la base de datos SQL que los contiene.
            contenido = "07793397052082,AUROLUO,17/05/2026,*"
            archivo_texto.write(contenido)

        # Incrementar el contador
        contador += 1