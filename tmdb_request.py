from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# CORS-Konfiguration
origins = [
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TMDB-Konstanten
TMDB_URL = "https://api.themoviedb.org/3/discover/movie"
HEADERS = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZDlmNTBiNDg1NmIzNWRiNzczNzczODViZjgyYjAyMCIsIm5iZiI6MTc0NjgxMDQyNC42ODEsInN1YiI6IjY4MWUzNjM4Yzc5YzM1OWUzNGMxZTFhNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zE2heQbFHoiBFsPJqryPvqbPfY6Sqx_GTu35r3bQYYs",
    "Content-Type": "application/json;charset=utf-8"
}

# Pydantic-Modell für POST-Daten
class QueryParams(BaseModel):
    sort_by: str | None = None
    with_genres: str | None = None
    year: int | None = None
    language: str | None = "de-DE"
    page: int | None = 1

# Globale Vorschlagsliste (temporär)
suggestions = []

@app.post("/api/hallo")
def hallo(params: QueryParams):
    print("Empfangen vom Frontend:", params)

    # Anfrage an TMDB senden
    response = requests.get(TMDB_URL, headers=HEADERS, params=params.dict(exclude_none=True))

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail={"error": "TMDB Anfrage fehlgeschlagen", "details": response.text})

    # Ergebnisse verarbeiten
    results = response.json().get("results", [])[:10]
    for result in results:
        suggestions.append({
            "title": result.get("title"),
            "poster": f"https://image.tmdb.org/t/p/w500{result.get('poster_path')}",
            "overview": result.get("overview"),
            "rating": result.get("vote_average")
        })

    return {"antwort": suggestions}
