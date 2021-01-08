Proyecto 1:

Programa para obtener imágenes que contengan a los elementos de un archivo vectorial y sean extraídas de un ráster dado.
La salida del programa será un conjunto de subdirectorios distintos con una una imagen y un archivo txt que describa el punto vectorial contenido en dicha imagen.
Las imágenes generadas serán del mismo tamaño, están centradas en el centroide de la geometría correspondiente y, tendrán un radio de ancho y alto (buffer) definido por el usuario.

IMPORTANTE: el ráster original y el archivo vectorial (shp) debe estar en el mismo sistema coordenado y se recomienda altamente que este en unidades métricas

Para ejecutar el programa se debe hacer de la siguiente manera:

python3 main.py <ruta del ráster original>   <ruta del archivo vectorial>  <ruta del directorio donde se almacenaran todos los resultados (subdirectorios con imagen y txt)>   <buffer>

Ejemplo:

python3 main.py T14QMG_20201127T170641_TCI.jp2 estaciones-del-metroUTM.shp ResultadosXX 1500


**El archivo functions contiene funciones INDISPENSABLES para la ejecución del archivo main por lo que deben estar siempre juntos
