{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Proyecto 1:\
\
Programa para obtener im\'e1genes que contengan a los elementos de un archivo vectorial y sean extra\'eddas de un r\'e1ster dado.\
La salida del programa ser\'e1 un conjunto de subdirectorios distintos con una una imagen y un archivo txt que describa el punto vectorial contenido en dicha imagen.\
Las im\'e1genes generadas ser\'e1n del mismo tama\'f1o, est\'e1n centradas en el centroide de la geometr\'eda correspondiente y, tendr\'e1n un radio de ancho y alto (buffer) definido por el usuario.\
\
IMPORTANTE: el r\'e1ster original y el archivo vectorial (shp) debe estar en el mismo sistema coordenado y se recomienda altamente que este en unidades m\'e9tricas\
\
Para ejecutar el programa se debe hacer de la siguiente manera:\
\
python3 main.py <ruta del r\'e1ster original>   <ruta del archivo vectorial>  <ruta del directorio donde se almacenaran todos los resultados (subdirectorios con imagen y txt)>   <buffer>\
\
Ejemplo:\
\
python3 main.py T14QMG_20201127T170641_TCI.jp2 estaciones-del-metroUTM.shp ResultadosXX 1500\
\
\
**El archivo functions contiene funciones INDISPENSABLES para la ejecuci\'f3n del archivo main por lo que deben estar siempre juntos}