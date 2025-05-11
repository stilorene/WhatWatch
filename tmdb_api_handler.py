import requests

url = "https://api.themoviedb.org/3/discover/movie"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZDlmNTBiNDg1NmIzNWRiNzczNzczODViZjgyYjAyMCIsIm5iZiI6MTc0NjgxMDQyNC42ODEsInN1YiI6IjY4MWUzNjM4Yzc5YzM1OWUzNGMxZTFhNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zE2heQbFHoiBFsPJqryPvqbPfY6Sqx_GTu35r3bQYYs",  # <- Dein v4-Token hier einfügen
    "Content-Type": "application/json;charset=utf-8"
}
#Recht einfach das sind alle Parameter die ich übergeben kann, um damit nach einem passenden Film zu suchen
params = {
    "language": "de",
    "sort_by": "popularity.desc",
    "vote_count.gte": 100,
    # "vote_average.gte": 7
    "year": 2022
}

response = requests.get(url, headers=headers, params=params)
datas = response.json()

# Ausgabe ersten 10 Filmen
counter = 0
for result in datas["results"]: 
    counter += 1
    print(result)
    if counter >= 10:
        break

# print(datas["results"][0])
