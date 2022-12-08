import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dataframe import df_plat

app = FastAPI()

#Creamos la Api

@app.get("/",response_class=HTMLResponse)
async def index():
    return """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PI Engineering</title>
</head>
<body>
    <h1>Bienvenido al sistema de consultas de Plataformas</h1>
    <h2>Realiza todas las consultas que desees</h2> 
    <p>Consejo: colocar las plataformas con mayuscula y tipo como se indica entre ()<p>
    <br/>
    <h3>Para obtener la pelicula/serie de mayor duracion para una plataforma y año determinado, como asi tambien el titulo de la misma:</h3>
    <p>/get_max_duration/plataforma/año/tipo (min / seasons) - Por ej: /get_max_duration/Hulu/2018/min</p>
    <br/>
    <h3>Para obtener la cantidad de peliculas y series de una determinada plataforma:</h3>
    <p>/get_count_platform/plataforma - Por ej: /get_count_platform/Netflix</p>
    <br/>
    <h3>Para obtener la plataforma que contiene mas veces un genero con la cantidad respectiva:</h3>
    <p>/get_listedin/genero - Por ej: /get_listedin/Romantic</p>
    <br/>
    <h3>Para conocer el actor/actriz que mas aparecio en una plataforma y año determinado:</h3>
    <p>/get_actor/plataforma/año - Por ej: /get_actor/Netflix/2018</p>
    <br/>
    <h3>Para volver, elimine los decoradores</h3>
</body>
</html>"""

@app.get("/get_max_duration/{plataforma}/{anio}/{tipo}")
async def get_max_duration(plataforma:str, anio:int, tipo:str):    
    if tipo == 'min':
        t = 'Movie'
        g = df_plat[df_plat['plataforma'] == plataforma][df_plat['release_year'] == anio][df_plat['type'] == t].groupby(['plataforma', 'type', 'release_year'])['duration'].idxmax().tolist()
        duracion = df_plat['duration'].get(g[0])
        titulo = df_plat['title'].get(g[0])
    if tipo == 'seasons':
        t = 'TV Show'
        g = df_plat[df_plat['plataforma'] == plataforma][df_plat['release_year'] == anio][df_plat['type'] == t].groupby(['plataforma', 'type', 'release_year'])['duration'].idxmax()
        duracion = df_plat['duration'].get(g[0])
        titulo = df_plat['title'].get(g[0])
    return (f'La maxima duracion en {tipo} para un {t} de {plataforma} en el {anio} es: {duracion}, y el titulo de la misma es: {titulo}') 

@app.get("/get_count_platform/{plataforma}")
async def get_count_plataform(plataforma):
    c = df_plat[df_plat['plataforma'] == plataforma].groupby(['plataforma', 'type'])['type'].value_counts()
    return (f'La cantidad total de Movies para {plataforma} es: {c[0]}\
    La cantidad total de Tv Show para {plataforma} es: {c[1]}') 

@app.get("/get_listedin/{genero}")
async def get_listedin(genero):
    count= df_plat[df_plat.listed_in.str.contains(genero, case=False)].groupby(by=['plataforma']).title.count().sort_values(ascending= False).to_dict()
    claves = list(count.keys())
    valores = list(count.values())
    return f'El género {genero} aparece mas veces en la plataforma {claves[0]} con un total de: {valores[0]} veces'

@app.get("/get_actor/{plataforma}/{anio}")
async def get_actor(plataforma, anio): 
    actor_list = []
    cast_list = df_plat.query(f"plataforma == '{plataforma}' and release_year == {anio}").cast.tolist()
    for i in range(len(cast_list)):
        actor_list_temp = cast_list[i].split(",")
        for j in range(len(actor_list_temp)):
            if actor_list_temp[j] != 'None':
                actor_list.append(actor_list_temp[j])
    dict_actor = dict(zip(actor_list,map(lambda x: actor_list.count(x),actor_list)))
    max_actor = max(dict_actor, key=dict_actor.get)
    max_actor_appearances = dict_actor.get(max_actor)
    return f'El actor/actriz con mayor número de apariciones en la plataforma {plataforma} el año {anio} es {max_actor} con {max_actor_appearances} apariciones.'

if __name__ == '__main__':
    uvicorn.run(app, port=80)
