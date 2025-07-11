from flask import Flask, render_template, request, redirect, send_file, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from datetime import datetime
import pandas as pd
import pytz
import os

app = Flask(__name__)
app.secret_key = 'clave_segura_2025'

# 🔐 Configuración de Login
login_manager = LoginManager()
login_manager.init_app(app)

class Usuario(UserMixin):
    def __init__(self, id):
        self.id = id

usuarios_validos = {
    'admin': 'super123'
}

@login_manager.user_loader
def load_user(user_id):
    return Usuario(user_id)

# 📝 Ruta de registro público
@app.route('/')
def formulario():
    return render_template('formulario.html')

# 📥 Guardado de jornada
@app.route('/registrar', methods=['POST'])
def registrar():
    rut = request.form['rut']
    nombre = request.form['nombre']
    turno = request.form['turno']
    pieza = request.form['pieza']
    tipo = request.form['tipo']

    zona_chile = pytz.timezone('America/Santiago')
    fecha = datetime.now(zona_chile).strftime('%Y-%m-%d %H:%M:%S')

    nuevo = pd.DataFrame([[rut, nombre, turno, pieza, tipo, fecha]],
                         columns=['RUT', 'Nombre', 'Turno', 'Pieza', 'Marcación', 'FechaHora'])

    archivo = 'registro.xlsx'
    if os.path.exists(archivo):
        existente = pd.read_excel(archivo)
        final = pd.concat([existente, nuevo], ignore_index=True)
    else:
        final = nuevo

    final.to_excel(archivo, index=False)
    return f"✅ Registro exitoso: {nombre} ({rut}) - {tipo} a las {fecha}"

# 🔑 Login solo para descargar registros
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['clave']
        if usuario in usuarios_validos and clave == usuarios_validos[usuario]:
            login_user(Usuario(usuario))
            return redirect('/descargar')
        else:
            return "❌ Usuario o contraseña incorrecta."
    return render_template('login.html')

# 🚪 Cierre de sesión
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

# 📥 Descarga protegida del Excel
@app.route('/descargar')
@login_required
def descargar_excel():
    archivo = 'registro.xlsx'
    if os.path.exists(archivo):
        return send_file(archivo, as_attachment=True)
    else:
        return "❌ No hay registros disponibles para descargar."
    app.run(debug=True)




