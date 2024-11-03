from flask import Blueprint, render_template
from ..models import Turma

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/cadastro_professor')
def cadastro_professor():
    return render_template('cadastro_professor.html')

@main.route('/cadastro_turma')
def cadastro_turma():
    return render_template('cadastro_turma.html')

@main.route('/cadastro_aluno')
def cadastro_aluno():
    return render_template('cadastro_aluno.html')

#rota para listar as turmas com bd
@main.route('/listar_turmas')
def listar_turmas():
    turmas = Turma.query.all()  # Busca todas as turmas do bbd
    return render_template('listar_turmas.html', turmas=turmas)
