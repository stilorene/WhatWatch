#Das Skript hier macht vorerst mal nichts, habe hiermit versucht zu arbeiten, zum Teil super aber 
#Main sollte im Web mehr auf Javascript setzen, das funktioniert einfacher und ohne unötige Umwege
#ich verwende dieses hier vl später nochmal wenn es ans Backend und der TMDB-Api geht

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Erlaubt Zugriffe von localhost:5500 (Frontend)

@app.route('/api/hallo', methods=['POST'])
def hallo():
    datas = request.get_json()
    print("Empfangen:", datas)  # Wird im VS-Codeterminal angezeigt. Nicht im Browser, da ist es anonym
    return jsonify({"antwort": datas}) #Wichtig, jeder Request (Anfrage) braucht ein Response (Antwort)
                                        # FE(Request an BE) -> BE(Empfängt) -> BE(Response an FE) -> FE(sagt danke)

if __name__ == '__main__':
    # CORS(app) 
    app.run(port=5000, debug=True)



