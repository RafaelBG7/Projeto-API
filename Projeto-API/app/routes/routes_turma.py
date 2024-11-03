from flask import Blueprint, jsonify, request
from ..models import Turma, db

turma_blueprint = Blueprint('turma', __name__)

@turma_blueprint.route('', methods=['POST'])
def create_turma():
    data = request.get_json()
    nova_turma = Turma(
        descricao=data['descricao'], 
        professor_id=data['professor_id'], 
        ativo=data.get('ativo', True)
    )
    db.session.add(nova_turma)
    db.session.commit()
    return jsonify({'message': 'Turma criada com sucesso'}), 201

@turma_blueprint.route('', methods=['GET'])
def listar_turmas():
    turmas = Turma.query.all()
    return jsonify([{
        'id': turma.id,
        'descricao': turma.descricao,
        'ativo': turma.ativo,
        'professor': {
            'id': turma.professor.id,
            'nome': turma.professor.nome,
            'materia': turma.professor.materia
        },
        'alunos': [{'id': aluno.id, 'nome': aluno.nome} for aluno in turma.alunos]
    } for turma in turmas])

@turma_blueprint.route('/<int:id>', methods=['DELETE'])
def excluir_turma(id):
    turma = Turma.query.get(id)
    if turma:
        db.session.delete(turma)
        db.session.commit()
        return jsonify({'message': 'Turma excluída com sucesso'}), 200
    return jsonify({'error': 'Turma não encontrada'}), 404
