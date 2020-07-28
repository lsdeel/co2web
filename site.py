import os
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point


co2measdir='data/co2meas.csv'
co2sitesdir='output/gis/vector/co2sites.shp'

co2meas=pd.read_csv(co2measdir)
co2sites=co2meas[['Lat','Long','siteNo']].groupby(['siteNo'],as_index=False).first()

gpd.GeoDataFrame(co2sites,\
    geometry=[Point(xy) for xy in zip(co2sites.Long, co2sites.Lat)])

[Point(xy) for xy in zip(co2sites.Long, co2sites.Lat)]