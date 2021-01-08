import numpy as np
import rasterio
from osgeo import gdal, osr
#import matplotlib.pyplot as plt
import geopandas as gpd
from os import mkdir
import sys

import functions

ruts = sys.argv 


if len(ruts)>1:
    img2=rasterio.open(ruts[1])
    EPSG=int(str(img2.read_crs()).split(":")[1])
    ggt = tuple(img2.get_transform())
    data = img2.read(1)

    """pol=gpd.read_file("/Users/rauldelarosa/Desktop/Septimo/Progra/Proyecto/shp/areas-naturales-protegidas/areas-naturales-protegidas.shp", 
                    encoding='utf8')
    pol=pol.to_crs({'init':'epsg:32614'})"""

    pol=gpd.read_file(ruts[2],encoding='utf8')
    #pol=pol.to_crs('epsg:32614')

    xy=functions.getCentroids(pol)
    x=xy[0]
    y=xy[1]
    
    try:
        mkdir(ruts[3])
        dirP=ruts[3]
    except IndexError:
        mkdir("Resultados")
        dirP=ruts["Resultados"]
    except:
        dirP=ruts[3]

    try:
        buffer=int(ruts[4])
    except IndexError:
        buffer=500


    for row,cx,cy in zip(pol.itertuples(),x,y):

        offsetx=np.random.choice([2,-2],1)[0]
        offsety=np.random.choice([2,-2],1)[0]

        cx+=(offsetx)*np.hypot(buffer,buffer)
        cy+=(offsety)*np.hypot(buffer,buffer)

        res=functions.subImage(cx,cy,buffer,data,ggt)

        if res:
            txt=""
            for col,i in zip(pol.columns[:-1],range(0,len(pol.columns[:-1]))):
                nid=str(int(row[0]))
                txt+=col+": "+str(row[i])+"\n"
            txt+="x: {:.3f}\n".format(cx)
            txt+="y: {:.3f}\n".format(cy)

            dirName ="ID_"+nid+"_X_"+str(round(cx))+"_Y_"+str(round(cy))+"_B_"+str(round(buffer))
            try:
                mkdir(dirP+"/"+dirName)
            except:
                pass

            with open(dirP+"/{}/{}.txt".format(dirName,dirName),"w") as f:
                f.write(txt)

            functions.saveTif(res,dirP+"/{}/{}".format(dirName,dirName),EPSG)

else:
    print("ingrese rutas")