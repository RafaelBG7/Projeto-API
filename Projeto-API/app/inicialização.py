# app/inicialização.py
from flask import Flask
from app.database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)

    from .routes.routes_aluno import aluno_blueprint
    from .routes.routes_professor import professor_blueprint
    from .routes.routes_turma import turma_blueprint
    from .routes.main import main

    app.register_blueprint(aluno_blueprint, url_prefix='/alunos')
    app.register_blueprint(professor_blueprint, url_prefix='/professores')
    app.register_blueprint(turma_blueprint, url_prefix='/turmas')
    app.register_blueprint(main)

    return app
