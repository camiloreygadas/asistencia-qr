import qrcode
url = "http://192.168.1.158:5000/"  # Reemplaza con tu IP real
qr = qrcode.make(url)
qr.save("qr_asistencia.png")
print("✅ Código QR generado como 'qr_asistencia.png'")
