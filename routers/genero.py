from flask import request,render_template
from models.genero import Genero
from app import app

@app.route("/listargenero/",methods=['GET'])
def listGenero():
    try:
        mensaje=None
        generos=Genero.objects()
    except Exception as error:
        mensaje=str(error)
    return render_template('listargenero.html',mensaje=mensaje,generos=generos)
    
@app.route("/agregargenero/",methods=['GET'])
def addGenero():
    try:
        mensaje=None
        estado=False
        if request.method=='POST':
            datos=request.get_json(force=True)
            genero=Genero(**datos)
            genero.save()
            estado=True
            mensaje="Genero Agregado correctamente"
        else:
            mensaje="No permitido"
    except Exception as error:
        mensaje=str(error)
    return render_template('agregargenero.html',estado=estado,mensaje=mensaje)
        