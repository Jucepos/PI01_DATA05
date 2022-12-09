# <h1 align=center> **Bienvenidos a mi PI - Data Engineering** :construction_worker:</h1>

INTRODUCCIÓN: :arrow_down:

Mi nombre es Julio Postigo, en este caso vengo a mostrar un proyecto realizado en la etapa de Labs del curso de Data Science de Henry. 

En esta oportunidad el proyecto consistia en una limpieza de datos a partir de 4 fuentes de datos distintas (3 archivos csv y 1 archivo json).

Para el mismo decidi usar durante todo el proceso de ETL la libreria pandas.

Con la misma tambien cree las funciones adecuadas para llevar a cabo las consultas.

En este repo encontraran:

🔸 Archivo principal: app/main.py

🔸 Archivo con etl comentado: app/main.ipynb

🔸 Archivo con los datasets: app/datasets/

🔸 Archivo para obtencion del dataframe final: app/dataframe.py
***
OBJETIVOS: :arrow_down:

Realizar una ingesta de datos (archivos de diferentes extensiones, como csv o json), posteriormente aplicar las transformaciones pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API estará construida en un entorno virtual dockerizado.

Las consultas a realizar son:

🔸 Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser: get_max_duration(año, plataforma, [min o season])

🔸 Cantidad de películas y series (separado) por plataforma El request debe ser: get_count_plataform(plataforma)

🔸 Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser: get_listedin('genero')

🔸 Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)
***
:bangbang: Link de acceso a la api :bangbang:

pi01-data05-prod-pi-engineering-cb1jq9.mo2.mogenius.io:80
***
:bangbang: Link del video explicativo :bangbang:
https://www.youtube.com/watch?v=a3-S00GrfPE&ab_channel=JulioPostigo

***
Herramientas utilizadas: :arrow_down:

🔸 Python

🔸 Pandas

🔸 Docker

🔸 FastAPI

🔸Mogenius
