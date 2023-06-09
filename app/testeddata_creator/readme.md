Esta sección de la aplicación convertirá las imágenes contenidas en el directorio "fotos" en imágenes
en escala de grises, cambiara su extension a .tiff y las enumerara de forma correlativa. Luego agregara 
estas imagenes con la nueva extension a una carpeta llamada "images".

También creará un directorio "gt" donde se guardaran la información que debería contener cada imagen en archivos 
individuales cuyo nombre es el mismo que la imagen a la que representan. Su extensión debe ser .gt.txt. 

En este momento, los datos que iran en los archivos "gt" son simples, ya que se omite el último campo variable 
y solo se ingresa información sobre campos fijos.

En un futuro, estos archivos "gt" podrían contener toda la información sobre los campos a decodificar en la imagen,
ya que los mismos se encuentran en una base de datos SQL. Por el momento se hará una prueba sencilla con los otros
3 campos. 

Tenemos que crear un directorio "fonts" que contenga las fuentes que fueron utilizadas para imprimir los campos 
sobre los estuches. 

Tenemos que crear un directorio "langdata" que contiene el archivo de configuración de idioma. 
