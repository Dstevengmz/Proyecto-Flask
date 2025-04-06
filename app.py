from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask import session, flash
import os
from dotenv import load_dotenv
app = Flask(__name__)  
app.config['SECRET_KEY'] = 'darwin'
CORS(app)
app.config["UPLOAD_FOLDER"] = "./static/img"
# app.config["MONGODB_SETTINGS"] = [{
#     "db": "GestionPeliculas",
#     "host": "mongodb+srv://dstevengmz1293:<db_password>@cluster0.6jt6j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
#     "port": 27017
# }]
app.config["MONGODB_SETTINGS"] = [{
    "db": "GestionPeliculas",
    "host": os.getenv("MONGO_URI"),
    "port": 27017
}]

db = MongoEngine(app)

from routers.genero import *
from routers.pelicula import * 
from routers.login import * 
from routers.usuario import * 

if __name__ == "__main__":
    app.run(port=6510, host="0.0.0.0", debug=True)
