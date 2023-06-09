import subprocess
# import os
# import pytesseract


dir = 'D:/gitProyects/ocr-reader-tesseract/app/testeddata_creator'
output_base_name = 'test1'

# Ejecuta el comando de entrenamiento de Tesseract
command = [
    r'C:\Program Files (x86)\Tesseract-OCR-3-5-0\tesseract.exe',
    f'{dir}/images/',
    f'{dir}/{output_base_name}',
    '--psm',
    '4',
    'nobatch'
]

subprocess.run(command)

# print(pytesseract.get_tesseract_version())