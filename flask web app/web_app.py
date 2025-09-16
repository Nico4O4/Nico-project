from flask import Flask #flask importieren

meine_app = Flask(__name__) #flask app erstellen (instanz)

@meine_app.route("/") #route -> für die route welche URL flask nutzen soll zzb. site/home/login etc.
def hello_world(): #nachricht im browser anzeigen
    return "<p>Haii World</p>" #nachricht in HTML format als string