Proyecto 2:

Programa para obtener imágenes que NO contengan a los elementos de un archivo vectorial y sean extraídas de un ráster dado.
La salida del programa será un conjunto de subdirectorios distintos con una una imagen que en principio no debe contener ningún punto  (centroide si el archivo vectorial corresponde a polígonos) de shp ingresado.
Las imágenes generadas serán del mismo tamaño y tendrán un radio de ancho y alto (buffer) definido por el usuario. 
El usuario debe ingresar un buffer de referencia para que las imágenes resultantes no estén dentro de ese radio (se recomienda sea equivalente al buffer ingresado en el proyecto 1). 
Vale la pena mencionar que existe la posibilidad de que alguna de las imágenes contenga algún punto o parte de su buffer que este cercano al punto que tiene como referencia, de ser el caso, se buscará que esa imagen tenga el mínimo de coincidencias pues, el programa funciona mediante la búsqueda aleatoria de posiciones para el ráster resultante.

IMPORTANTE: el ráster original y el archivo vectorial (shp) debe estar en el mismo sistema coordenado y se recomienda altamente que este en unidades métricas

Para ejecutar el programa se debe hacer de la siguiente manera:

python3 main.py <ruta del ráster original>   <ruta del archivo vectorial>  <ruta del directorio donde se almacenaran todos los resultados (subdirectorios con imagen)>   <buffer de las nuevas imagenes>  <buffer de los puntos referentes del archivo vectorial>

Ejemplo:

python3 main.py T14QMG_20201127T170641_TCI.jp2 estaciones-del-metroUTM.shp  ResultadosXX 500  200


**El archivo functions contiene funciones INDISPENSABLES para la ejecución del archivo main por lo que  siempre deben estar juntos
