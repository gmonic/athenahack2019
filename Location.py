# This project is developed as part of the Athena Hackathon 2019 competition.
# This script includes the code that identifies your location and shows the directions to the nearest recycling station.

# Author: Dr Eirini Mavroudi
# Date: 13/04/2019
########################################################################################################################

# Import libraries

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import geopandas as gpd
from geopandas import GeoSeries, GeoDataFrame
from shapely.geometry import Point

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/Map')
def Map():
    # Input Geographical data
    loc = gpd.read_file("ba_pop_2014.shp")

    # Input data for recycling stations
    recycle_stations_coord = pd.read_csv("http://cdn.buenosaires.gob.ar/datosabiertos/datasets/centros-de-clasificacion-de-residuos/centros-de-clasificacion-de-residuos.csv")

    # Convert data for recycling stations to points.
    rec_stations = GeoDataFrame(recycle_stations_coord.assign(geometry = lambda x: x.apply(lambda x: Point(float(x['long']), float(x['lat'])), axis=1)))

    # Plot the maps!
    ax = loc.plot(color='red')
    rec_stations.plot(ax=ax, alpha=0.5, color='black')
    return "Done"



# In order to run this function that is created by Flask, you need to export it first via:
# export FLASK_APP = Location.py

# In order to export this as a website application you need to run this using the command:
# python -m flask run

# Then you need to copy the browser address in your browser so as to see the results.
