from flask import render_template, request, jsonify, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from app import app
from models.usuario import Usuario 
import app as dbase


# Ruta de Login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario_input = request.form['usuario']
        contrasena_input = request.form['clave']
        usuario_db = Usuario.objects(usuario=usuario_input).first()
        if usuario_db and check_password_hash(usuario_db.password, contrasena_input):
            session['usuario_id'] = str(usuario_db.id)
            session.permanent = True
            flash('Inicio sesion correcto', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciales incorrectas. Intenta nuevamente.', 'error')
            return redirect(url_for('index'))
    return render_template('login.html')

#cerrar sesión
@app.route('/logout')
def logout():
    session.pop('usuario_id', None)
    flash('¡Has cerrado sesión!', 'info')
    return redirect(url_for('login'))
