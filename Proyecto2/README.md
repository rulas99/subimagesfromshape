{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Proyecto 2:\
\
Programa para obtener im\'e1genes que NO contengan a los elementos de un archivo vectorial y sean extra\'eddas de un r\'e1ster dado.\
La salida del programa ser\'e1 un conjunto de subdirectorios distintos con una una imagen que en principio no debe contener ning\'fan punto  (centroide si el archivo vectorial corresponde a pol\'edgonos) de shp ingresado.\
Las im\'e1genes generadas ser\'e1n del mismo tama\'f1o y tendr\'e1n un radio de ancho y alto (buffer) definido por el usuario. \
El usuario debe ingresar un buffer de referencia para que las im\'e1genes resultantes no est\'e9n dentro de ese radio (se recomienda sea equivalente al buffer ingresado en el proyecto 1). \
Vale la pena mencionar que existe la posibilidad de que alguna de las im\'e1genes contenga alg\'fan punto o parte de su buffer que este cercano al punto que tiene como referencia, de ser el caso, se buscar\'e1 que esa imagen tenga el m\'ednimo de coincidencias pues, el programa funciona mediante la b\'fasqueda aleatoria de posiciones para el r\'e1ster resultante.\
\
IMPORTANTE: el r\'e1ster original y el archivo vectorial (shp) debe estar en el mismo sistema coordenado y se recomienda altamente que este en unidades m\'e9tricas\
\
Para ejecutar el programa se debe hacer de la siguiente manera:\
\
python3 main.py <ruta del r\'e1ster original>   <ruta del archivo vectorial>  <ruta del directorio donde se almacenaran todos los resultados (subdirectorios con imagen)>   <buffer de las nuevas imagenes>  <buffer de los puntos referentes del archivo vectorial>\
\
Ejemplo:\
\
python3 main.py T14QMG_20201127T170641_TCI.jp2 estaciones-del-metroUTM.shp  ResultadosXX 500  200\
\
\
**El archivo functions contiene funciones INDISPENSABLES para la ejecuci\'f3n del archivo main por lo que  siempre deben estar juntos}