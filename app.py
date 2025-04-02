from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask import session, flash

app = Flask(__name__)  
app.config['SECRET_KEY'] = 'darwin'
CORS(app)
app.config["UPLOAD_FOLDER"] = "./static/img"
app.config["MONGODB_SETTINGS"] = [{
    "db": "GestionPeliculas",
    "host": "localhost",
    "port": 27017
}]

db = MongoEngine(app)

if __name__ == "__main__":
    from routers.genero import *
    from routers.pelicula import * 
    from routers.login import * 
    from routers.usuario import * 
    app.run(port=6510, host="0.0.0.0", debug=True)
