from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Crear la instancia de SQLAlchemy fuera de la funcin create_app
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@db:3306/app'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Deshabilitar el seguimiento de modificaciones

    # Inicializar la extensión SQLAlchemy con la aplicación Flask
    db.init_app(app)

    class Usuario(db.Model):
        __tablename__ = 'usuario'
        id = db.Column(db.Integer, primary_key=True)
        nombre = db.Column(db.String(255), nullable=True)
        apellido = db.Column(db.String(255), nullable=True)

    @app.route('/')
    def index():
        usuarios = Usuario.query.all()
        return render_template('index.html', usuarios=usuarios)

    @app.route('/crear_usuario', methods=['GET', 'POST'])
    def crear_usuario():
        if request.method == 'POST':
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            usuario = Usuario(nombre=nombre, apellido=apellido)
            db.session.add(usuario)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('crear_usuario.html')

    @app.route('/editar_usuario/<int:id>', methods=['GET', 'POST'])
    def editar_usuario(id):
        usuario = Usuario.query.get_or_404(id)
        if request.method == 'POST':
            usuario.nombre = request.form['nombre']
            usuario.apellido = request.form['apellido']
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('editar_usuario.html', usuario=usuario)

    @app.route('/eliminar_usuario/<int:id>', methods=['POST'])
    def eliminar_usuario(id):
        usuario = Usuario.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return redirect(url_for('index'))

    return app

if __name__ == '__main__':
    app = create_app()

    # Crear todas las tablas en la base de datos
    with app.app_context():
        db.create_all()

    # Ejecutar la aplicacin
    app.run(debug=True, host='0.0.0.0')
