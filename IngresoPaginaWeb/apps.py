from django.apps import AppConfig
from flask import Flask, request, render_template
app = Flask(__name__)


class IngresopaginawebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'IngresoPaginaWeb'

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')
        # Aquí puedes guardar los datos en tu base de datos
        # Por ahora, solo los imprimiremos en la consola
        print(f'Nombre: {nombre}, Correo: {correo}, Contraseña: {contrasena}')
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=False)