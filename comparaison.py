import sqlite3
from carteStation import carte
import folium
import itertools
from scipy.spatial import Delaunay
import numpy as np
import sqlite3
import json
db = sqlite3.connect("./station.db")
cursor=db.cursor()

unique1=[]
unique2=[]


temperature=[(a[0],json.loads(a[1])) for a in cursor.execute('SELECT station_id,position FROM temperature').fetchall()]
precipitation=[(a[0],json.loads(a[1])) for a in cursor.execute('SELECT station_id,position FROM precipitation').fetchall()]

for element in temperature:
    if element not in precipitation and element not in unique1:
        unique1.append(element)
        
for element in precipitation:
    if element not in temperature and element not in unique2:
        unique2.append(element)




db = sqlite3.connect("./station.db")
cursor=db.cursor()

map_center=[np.float64(45.98559729035534), np.float64(3.3209267324873104)]
mymap = folium.Map(location=map_center, zoom_start=2)
def carte(sta,color):
    stations=sta
    for station in stations:
        folium.Marker(
            location=[station[1][0], station[1][1]],
            icon=folium.Icon(color=color)
        ).add_to(mymap)


carte(unique1,'blue')
carte(unique2,'red')

mymap.save("triangles_map2.html")