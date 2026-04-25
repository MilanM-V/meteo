import requests
from regiondptsfrance import*
import sqlite3
import json
import time
db = sqlite3.connect("./station.db")
cursor=db.cursor()

#creer les tables et leur attributs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS precipitation (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        station_id INTEGER DEFAULT NULL,
        nom TEXT DEFAULT NULL,
        posteOuvert TEXT DEFAULT NULL,
        typePoste INTEGER DEFAULT NULL,
        numDepartement INTEGER DEFAULT NULL,
        position TEXT DEFAULT NULL
    );
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS temperature (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        station_id INTEGER DEFAULT NULL,
        nom TEXT DEFAULT NULL,
        posteOuvert TEXT DEFAULT NULL,
        typePoste INTEGER DEFAULT NULL,
        numDepartement INTEGER DEFAULT NULL,
        position TEXT DEFAULT NULL
    );
''')
#clee api (a update)
api_key='eyJ4NXQiOiJZV0kxTTJZNE1qWTNOemsyTkRZeU5XTTRPV014TXpjek1UVmhNbU14T1RSa09ETXlOVEE0Tnc9PSIsImtpZCI6ImdhdGV3YXlfY2VydGlmaWNhdGVfYWxpYXMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJtaWxhbi5tdkBjYXJib24uc3VwZXIiLCJhcHBsaWNhdGlvbiI6eyJvd25lciI6Im1pbGFuLm12IiwidGllclF1b3RhVHlwZSI6bnVsbCwidGllciI6IlVubGltaXRlZCIsIm5hbWUiOiJEZWZhdWx0QXBwbGljYXRpb24iLCJpZCI6MjY1MDcsInV1aWQiOiI3ZDgzZWQ3My1iMTU2LTQyNTItYmMxNi1kNzFhYTYyMGY5YjUifSwiaXNzIjoiaHR0cHM6XC9cL3BvcnRhaWwtYXBpLm1ldGVvZnJhbmNlLmZyOjQ0M1wvb2F1dGgyXC90b2tlbiIsInRpZXJJbmZvIjp7IjUwUGVyTWluIjp7InRpZXJRdW90YVR5cGUiOiJyZXF1ZXN0Q291bnQiLCJncmFwaFFMTWF4Q29tcGxleGl0eSI6MCwiZ3JhcGhRTE1heERlcHRoIjowLCJzdG9wT25RdW90YVJlYWNoIjp0cnVlLCJzcGlrZUFycmVzdExpbWl0IjowLCJzcGlrZUFycmVzdFVuaXQiOiJzZWMifX0sImtleXR5cGUiOiJQUk9EVUNUSU9OIiwic3Vic2NyaWJlZEFQSXMiOlt7InN1YnNjcmliZXJUZW5hbnREb21haW4iOiJjYXJib24uc3VwZXIiLCJuYW1lIjoiRG9ubmVlc1B1YmxpcXVlc0NsaW1hdG9sb2dpZSIsImNvbnRleHQiOiJcL3B1YmxpY1wvRFBDbGltXC92MSIsInB1Ymxpc2hlciI6ImFkbWluX21mIiwidmVyc2lvbiI6InYxIiwic3Vic2NyaXB0aW9uVGllciI6IjUwUGVyTWluIn1dLCJleHAiOjE3NjI2ODcyNzQsInRva2VuX3R5cGUiOiJhcGlLZXkiLCJpYXQiOjE3NTI2ODcyNzQsImp0aSI6ImE3NjI1ZDQ2LWZlYzAtNDUyYy1iMTZlLTRhYmY3MmUyZDQzYiJ9.oGOnri2Ki_tChEWNWvSKj8ggYOjmMSnKEHFxzjfgTmTXIaVzFUbOog1Ax5i-Q3auLlIbtN1f1BSvAMufCWlS4pING6drJBV5q6fghTBUJVPB8w03GJf_KCcrYzmVgZ4a4h6CYNYlN8kUks_TLwTzC4IZBXVDRdskp9MmgYrC_w1yY0ACXFpktCNsarMNIyBJPzKf3gQHQiObXAddffYDBe3FT0wWL6NgIxbxbh2Flc0UmDA06v0LFFPak5HaIsPiIgINWBdiPk2OyK7bs1wbn8-DaMFBW8i5x_4wxEfWMDtmFwJxcA0mk4GT5NscXZkJVMoPoiwfdeuIXEIgFFVpfA=='
parametres=['temperature','precipitation']


def limite(data,search_url,response):
    """
    -fonction limite qui a pour parametre l'url de requete, le code reponse de la requete et les donnees recuperer
    -la fonction verifie si on ne depasse pas la limite de cota imposer par l'api
    """
    quota=False
    if response.status_code !=200:
        quota=True
    if quota==True:
        time.sleep(2)
        response = requests.get(search_url,headers={'accept': '*/*',"apikey":api_key})
        data = response.json()
        limite(data,search_url,response)
    else:
        return True
    
for parametre in parametres:
    for departement in DEPARTMENTS.keys():
        search_url = f"https://public-api.meteofrance.fr/public/DPClim/v1/liste-stations/quotidienne?id-departement={departement}&parametre={parametre}"   
        response = requests.get(search_url,headers={'accept': '*/*',"apikey":api_key})
        data = response.json()
        if limite(data,search_url,response):
            for element in data:
                if element['typePoste']<5 and element['posteOuvert']==True:
                    cursor.execute(f'INSERT INTO {parametre} (station_id,nom,posteOuvert,typePoste,numDepartement,position) VALUES (?,?,?,?,?,?)',(element['id'],element['nom'],element['posteOuvert'],element['typePoste'],departement,json.dumps([element['lat'],element['lon']]),))

    
db.commit()

db.close()
