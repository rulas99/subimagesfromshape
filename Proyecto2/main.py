import numpy as np
import rasterio
from osgeo import gdal, osr
#import matplotlib.pyplot as plt
import geopandas as gpd
from os import mkdir
import sys
from copy import copy

import functions

ruts = sys.argv 


if len(ruts)>1:
    img2=rasterio.open(ruts[1])
    EPSG=int(str(img2.read_crs()).split(":")[1])
    ggt = tuple(img2.get_transform())
    data = img2.read(1)

    pol=gpd.read_file(ruts[2],encoding='utf8')

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
        buffer=300

    try:
        bufferPT=int(ruts[5])
    except IndexError:
        bufferPT=copy(buffer)

    d=buffer+bufferPT
    hypPT=np.hypot(bufferPT,bufferPT)
    offset=[-1,-1.5,1,1.5,2,-2,0,2.5,-2.5,3,-3,3.5,-3.5,4,-4]

    """try:
        trys=int(ruts[5])
    except IndexError:
        trys=round((len(x)*11)/2)"""

    trys=int((len(x)*len(offset))/20)

    for row,cx,cy in zip(pol.itertuples(),x,y):

        v=0
        maxv=0
        while v!=len(x)*trys:

            offsetx=np.random.choice(offset,1)[0]
            if offsetx==0:
                offsety=np.random.choice(copy(offset).remove(0),1)[0]
            else:
                offsety=np.random.choice(offset,1)[0]

            cxO=cx+(offsetx*np.hypot(d,d))
            cyO=cy+(offsety*np.hypot(d,d))

            #d=np.round(np.hypot(offsetx*np.hypot(buffer,buffer),offsety*np.hypot(buffer,buffer)))

            res1=functions.subImage(cxO,cyO,buffer,data,ggt)
            ##res=copy(res1)  

            c=0
            for vx,vy in zip(x,y):
                if functions.getIndex(vx,vy,res1[1],res1[0]):
                    break
                elif functions.getIndex(vx+hypPT,vy+hypPT,res1[1],res1[0]):
                    break
                elif functions.getIndex(vx+hypPT,vy-hypPT,res1[1],res1[0]):
                    break
                elif functions.getIndex(vx-hypPT,vy+hypPT,res1[1],res1[0]):
                    break
                elif functions.getIndex(vx-hypPT,vy-hypPT,res1[1],res1[0]):
                    break
                else:
                    c+=1
            
            if c>maxv:
                 res=copy(res1)  
                 maxv=copy(c)

            v+=1

            if c==len(x):
                res=copy(res1) 
                break


        """offsetx=np.random.choice([2,-2,0],1)[0]
        offsety=np.random.choice([2,-2,0],1)[0]

        cxO=cx+(offsetx)*np.hypot(buffer,buffer)
        cyO=cy+(offsety)*np.hypot(buffer,buffer)

        res=functions.subImage(cxO,cyO,buffer,data,ggt)"""


        if res:
            dirName ="X_"+str(int(round(cxO)))+"_Y_"+str(int(round(cyO)))+"_B_"+str(buffer)
            try:
                mkdir(dirP+"/"+dirName)
            except:
                pass

            functions.saveTif(res,dirP+"/{}/{}".format(dirName,dirName),EPSG)

else:
    print("ingrese rutas")