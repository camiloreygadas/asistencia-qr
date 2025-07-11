# Sistema de Registro de Jornada por QR 🕒📲

Este proyecto permite registrar la llegada y salida de trabajadores mediante escaneo de un código QR desde sus dispositivos móviles. El sistema está desarrollado en **Python con Flask**, y guarda los datos en formato Excel.

## 🎯 Características principales

- Escaneo de QR instalado en punto físico (faena, entrada de recinto, etc.)
- Formulario web responsivo compatible con celulares
- Registro de:
  - ✅ RUT
  - ✅ Nombre
  - ✅ Turno (5x2, 7x7, 14x14)
  - ✅ Pieza o habitación asignada
  - ✅ Tipo de marcación (Entrada / Salida)
  - ✅ Fecha y hora del registro
- Exportación automática a archivo Excel (`registro.xlsx`)
- Interfaz sencilla y moderna

## 🚀 Cómo ejecutar localmente

1. Instala los módulos requeridos:

   ```bash
   pip install flask pandas openpyxl

2. Ejecuta el servidor Flask:
python app.py

3. Accede en el navegador:
http://localhost:5000/

☁️ Despliegue en Render
Este sistema puede ser desplegado en Render para uso permanente online. Se incluye un archivo requirements.txt y Procfile para facilitar el proceso.

📁 Estructura del proyecto

asistencia_qr/
├── app.py
├── requirements.txt
├── Procfile
├── registro.xlsx
├── templates/
│   └── formulario.html

📦 Dependencias
Flask

pandas

openpyxl

gunicorn (para despliegue en Render)

✨ Autor
Jorge Reygadas Espinoza Encargado Liquidador de Haberes | Automatización y RRHH | Región de Coquimbo, Chile

