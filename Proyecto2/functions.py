import numpy as np
#import rasterio
from osgeo import gdal, osr
#import matplotlib.pyplot as plt
#import geopandas as gpd
from numba import njit

def getCentroids(pol):
    '''
    Funcion que obtiene los centroides de cada geometria en un GeoDataFrame
    @param pol: GeoDataFrame preferentemente en unidades metricas
    @return [x,y]: donde x,y son las listas de todas las coordenadas en x,y respectivamente
    '''
    x=list(pol['geometry'].centroid.x)
    y=list(pol['geometry'].centroid.y)
    return x,y

@njit
def getIndex(x,y,ggt,data)->list:
    '''
    Funcion que calcula el renglon y columna correspondientes a una coordenada
    @param x: coordenada en x
    @param y: coordenada en y
    @param data: matriz (numpy array) en la que se buscara el punto (x,y)
    @param ggt: geotransformacion en formato gdal de la imagen original
    @return: [renglon,columnna]
    '''
    if (x<ggt[0]) or (x>ggt[0]+ggt[1]*data.shape[0]) or (y>ggt[-3]) or (y<ggt[-3]+ggt[-1]*data.shape[1]):
        pass
    else:
        col=round((x-ggt[0])/ggt[1])
        row=round((y-ggt[-3])/ggt[-1])
        return [row,col]

@njit
def subImage(x,y,buffer,data,ggt)->tuple:
    '''
    Funcion que crea obtiene un subarreglo a partir de un coordenada x,y central y un buffer (en las mismas unidades que las coordenadas)
    @param x: coordenada en x
    @param y: coordenada en y
    @param buffer: radio (en las mismas unidades que las coordenadas) 
    correspondiente a la extensión de la imagen a partir de las x,y centrales
    @param data: matriz (numpy array) de la cual se extraera el subarreglo
    @param ggt: geotransformacion en formato gdal de la imagen origen de la cual se extrae el arreglo contenedor (list)
    @return: subarreglo (numpy array)
    '''
    
    leftUpCorner=getIndex(x-buffer,y+buffer,ggt,data)
    rightDownCorner=getIndex(x+buffer,y-buffer,ggt,data)
    
    if (leftUpCorner!=None) and (rightDownCorner!=None):
        try:
            sub=data[leftUpCorner[0]:rightDownCorner[0]+1,leftUpCorner[1]:rightDownCorner[1]+1]
            ggtSub=(x-buffer,ggt[1],0,y+buffer,0,ggt[-1])
            return sub,ggtSub
        except:
            pass

def saveTif(im,nom,EPSG):
    '''
    Función que crea un GeoTif
    @param im: np.array que contiene los datos de la imagen de forma matricial y la geotransformación
    @param nom: nombre (y ruta) con el que se guardara el tif resultante
    @param EPSG: EPSG de origen en el que se encuentra la geotransformación
    '''
    dst_ds = gdal.GetDriverByName('GTiff').Create(nom+'.tif', im[0].shape[1],  im[0].shape[0], 1, gdal.GDT_CFloat32)
    dst_ds.SetGeoTransform(im[1])    
    srs = osr.SpatialReference()           
    srs.ImportFromEPSG(EPSG) #EPSG de la imagen original
    dst_ds.SetProjection(srs.ExportToWkt())
    dst_ds.GetRasterBand(1).WriteArray(im[0])   
    dst_ds.FlushCache()                     

    dst_ds = None