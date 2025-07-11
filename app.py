from flask import Flask, render_template, request, send_file
from datetime import datetime
import pandas as pd
import os

app = Flask(__name__)

# Ruta para mostrar el formulario
@app.route('/')
def formulario():
    return render_template('formulario.html')

# Ruta para registrar datos
@app.route('/registrar', methods=['POST'])
def registrar():
    rut = request.form['rut']
    nombre = request.form['nombre']
    turno = request.form['turno']
    pieza = request.form['pieza']
    tipo = request.form['tipo']
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

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

# ✅ Ruta para descargar el archivo Excel
@app.route('/descargar')
def descargar_excel():
    archivo_excel = 'registro.xlsx'
    if os.path.exists(archivo_excel):
        return send_file(archivo_excel, as_attachment=True)
    else:
        return "❌ No hay registros disponibles para descargar."
    app.run(debug=True)




