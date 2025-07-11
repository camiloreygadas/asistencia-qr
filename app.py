from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from datetime import datetime
from io import BytesIO
import pandas as pd
import pytz
import os

app = Flask(__name__)
app.secret_key = 'clave_secreta_123'  # Cámbiala por una clave más segura

# 🔐 Configuración Login
login_manager = LoginManager()
login_manager.init_app(app)

class Usuario(UserMixin):
    def __init__(self, id):
        self.id = id

usuarios_validos = {
    'admin': 'tu_contraseña'  # Cambia esto por tu clave real
}

@login_manager.user_loader
def load_user(user_id):
    return Usuario(user_id)

# 📝 Ruta para el formulario
@app.route('/')
def formulario():
    return render_template('formulario.html')

# 📌 Ruta para guardar el registro
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

    archivo_excel = 'registro.xlsx'
    if os.path.exists(archivo_excel):
        existente = pd.read_excel(archivo_excel)
        final = pd.concat([existente, nuevo], ignore_index=True)
    else:
        final = nuevo

    final.to_excel(archivo_excel, index=False)
    return f"✅ Registro exitoso: {nombre} ({rut}) - {tipo} a las {fecha}"

# 🔒 Ruta de login
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

# 🔓 Ruta de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

# 📥 Ruta protegida para descargar el Excel
@app.route('/descargar')
@login_required
def descargar_excel():
    archivo_excel = 'registro.xlsx'
    if os.path.exists(archivo_excel):
        return send_file(archivo_excel, as_attachment=True)
    else:
        return "❌ No hay registros disponibles para descargar."

# 🧪 Ejecutar localmente con debug
if __name__ == '__main__':

    app.run(debug=True)




