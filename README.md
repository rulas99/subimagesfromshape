In this repository I present two programs to obtain subimages from a given a raster and a shapefile:

* In the first directory yo will find a script that extracts subimages that contains (in the center) all the points of a given shp 
python3 main.py <raster>   <shapefile>  <output directory>   <image radius>

* In the second directory yo will find a script that extracts subimages that doesnt contains the points of a given shp
python3 main.py <raster>   <shapefile>  <output directory>   <image radius>  <points buffer>
  
The motivitation of making this, is create training and testing datasets for computer vision algorithms

-Note: the image and the shapefile must be in the same coordinate system and I recommend that they be in a metric system.
