import subprocess

tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tesstrain_script = r'C:\Program Files\Tesseract-OCR\tesstrain.sh'
training_data_dir = r'D:\gitProyects\ocr-reader-tesseract\app\ttrain-v5-3-3'
output_dir = r'D:\gitProyects\ocr-reader-tesseract\app\ttrain-v5-3-3'

# Comando para ejecutar tesstrain.sh
command = [
    tesseract_path,
    tesstrain_script,
    '--fonts_dir', 'fonts',  # Directorio de fuentes
    '--lang', 'eng',  # Idioma
    '--linedata_only', '--langdata_dir', 'langdata',  # Directorio de datos de idioma
    '--tessdata_dir', 'tessdata',  # Directorio de datos de Tesseract
    '--output_dir', output_dir,  # Directorio de salida
    '--fontlist', 'Arial', 'Times New Roman',  # Lista de fuentes a utilizar
    '--save_box_tiff', '--maxpages', '100',  # Opciones adicionales
    '--langdata_dir', training_data_dir  # Directorio de datos de entrenamiento
]

# Ejecutar el comando
subprocess.run(command, shell=True)