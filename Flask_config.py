#Das Skript hier macht vorerst mal nichts, habe hiermit versucht zu arbeiten, zum Teil super aber 
#Main sollte im Web mehr auf Javascript setzen, das funktioniert einfacher und ohne unötige Umwege
#ich verwende dieses hier vl später nochmal wenn es ans Backend und der TMDB-Api geht

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import requests

url = "https://api.themoviedb.org/3/discover/movie"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZDlmNTBiNDg1NmIzNWRiNzczNzczODViZjgyYjAyMCIsIm5iZiI6MTc0NjgxMDQyNC42ODEsInN1YiI6IjY4MWUzNjM4Yzc5YzM1OWUzNGMxZTFhNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zE2heQbFHoiBFsPJqryPvqbPfY6Sqx_GTu35r3bQYYs",  # <- Dein v4-Token hier einfügen
    "Content-Type": "application/json;charset=utf-8"
}


app = Flask(__name__)
CORS(app)  # Erlaubt Zugriffe von localhost:5500 (Frontend)

#Das Skript hier macht vorerst mal nichts, habe hiermit versucht zu arbeiten, zum Teil super aber 
#Main sollte im Web mehr auf Javascript setzen, das funktioniert einfacher und ohne unötige Umwege
#ich verwende dieses hier vl später nochmal wenn es ans Backend und der TMDB-Api geht

from flask import Flask, request, jsonify
from flask_cors import CORS

import requests

url = "https://api.themoviedb.org/3/discover/movie"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZDlmNTBiNDg1NmIzNWRiNzczNzczODViZjgyYjAyMCIsIm5iZiI6MTc0NjgxMDQyNC42ODEsInN1YiI6IjY4MWUzNjM4Yzc5YzM1OWUzNGMxZTFhNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zE2heQbFHoiBFsPJqryPvqbPfY6Sqx_GTu35r3bQYYs",  # <- Dein v4-Token hier einfügen
    "Content-Type": "application/json;charset=utf-8"
}


app = Flask(__name__)
# Erlaube explizit 127.0.0.1:5500
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})  # Erlaubt Zugriffe von localhost:5500 (Frontend)


suggestions = [] #globale Liste
@app.route('/api/hallo', methods=['POST'])
def hallo():
    datas = request.get_json()
    print("Empfangen vom Frontend:", datas)

    # TMDB-API Call direkt hier mit den empfangenen Daten als Parameter
    response = requests.get(url, headers=headers, params=datas)

    if response.status_code != 200:
        return jsonify({"error": "TMDB Anfrage fehlgeschlagen", "details": response.text}), 500

    # daten empfangen, Nur Top 10 Ergebnisse zurückgeben
    results = response.json().get("results", [])[:10]
    
    #hier nur relevantes zur Liste hinzufügen
    for result in results:
        suggestions.append({
            "title": result.get("title"),
            "poster": f"https://image.tmdb.org/t/p/w500{result.get('poster_path')}",
            "overview": result.get("overview"),
            "rating": result.get("vote_average")
        })
        
        
       


    #Anzeige in der Konsole
    # return jsonify({"antwort": suggestions})
    return render_template("suggestion.html", suggestions=suggestions)

    



if __name__ == '__main__':
    
    app.run(port=5000, debug=True)









