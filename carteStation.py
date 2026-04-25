import folium
import itertools
from scipy.spatial import Delaunay
import numpy as np
import sqlite3
import json
db = sqlite3.connect("./station.db")
cursor=db.cursor()

map_center=[np.float64(45.98559729035534), np.float64(3.3209267324873104)]
mymap = folium.Map(location=map_center, zoom_start=2)
def carte(parametre,color):
    stations=[(json.loads(a[0]),a[1]) for a in cursor.execute(f'SELECT position,nom FROM {parametre}').fetchall()]

    for station in stations:
        folium.Marker(
            location=[station[0][0], station[0][1]],
            popup=station[1],
            icon=folium.Icon(color=color)
        ).add_to(mymap)


carte('temperature','blue')
carte('precipitation','red')

mymap.save("triangles_map.html")
