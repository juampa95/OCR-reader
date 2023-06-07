Hubo que hacer algunos cambios, ya que el software de los equipos de la empresa no pueden usar una versión
de tesseract mayor a 3.5.0, por lo que tuve que instalar esta versión anterior junto con una versión 
compatible de pytesseract. 

Como el proyecto se basa en mejorar el resultado de la decodificación que hacen los equipos, voy a intentar
mejorar los datos de entrenamiento ".traineddata". 

Tengo el archivo que se utiliza actualmente la empresa, por lo que este será el punto de partida o el 
llamado "modelo base" de comparación para ver si logro una mejora de resultados. 

Por otro lado, el software implementado en la empresa no detecta las áreas donde están los caracteres de forma 
automática (se hace de forma manual seleccionando rectángulos sobre una imagen de prueba), esto hace que sea más 
rapido y más preciso. La idea de la nueva implementación, es mejorar ambos aspectos, o por lo menos mejorar la 
precisión manteniendo o mejorando la velocidad de procesado. 

Para ser funcional, debe recibir la imagen, pre-procesarla y decodificarla en un máximo de 200 milisegundos. 