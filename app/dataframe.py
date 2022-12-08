import pandas as pd
import re

df_amazon = pd.read_csv('./datasets/amazon_prime_titles.csv')
df_disney = pd.read_csv('./datasets/disney_plus_titles.csv')
df_hulu = pd.read_csv('./datasets//hulu_titles.csv')
df_netflix = pd.read_json('./datasets//netflix_titles.json')

df_amazon = df_amazon[['show_id', 'type', 'title', 'cast', 'release_year', 'duration','listed_in']]
df_disney = df_disney[['show_id', 'type', 'title', 'cast', 'release_year', 'duration','listed_in']]
df_hulu = df_hulu[['show_id', 'type', 'title', 'cast', 'release_year', 'duration','listed_in']]
df_netflix = df_netflix[['show_id', 'type', 'title', 'cast', 'release_year', 'duration','listed_in']]

df_amazon['plataforma']= 'Amazon'
df_disney['plataforma']= 'Disney'
df_hulu['plataforma']= 'Hulu'
df_netflix['plataforma']= 'Netflix'

df_amazon["cast"].fillna("None", inplace = True) 
df_disney["cast"].fillna("None", inplace = True) 
df_hulu["cast"].fillna("None", inplace = True) 
df_hulu["duration"].fillna("0", inplace = True) 
df_netflix["cast"].fillna("None", inplace = True) 
df_netflix["duration"].fillna("0", inplace = True) 

frames = [df_amazon, df_disney, df_hulu, df_netflix]
df_plat = pd.concat(frames, ignore_index=True)

def extraer_num(columna):
    d = re.match(r"\d+", columna)
    if d:
      return int(d.group())
    else:
      return 0

df_plat["duration"] = df_plat["duration"].map(extraer_num)


