from flask import Blueprint, jsonify, request
from ..models import Professor, db

professor_blueprint = Blueprint('professor', __name__)

@professor_blueprint.route('', methods=['POST'])
def create_professor():
    data = request.get_json()
    novo_professor = Professor(
        nome=data['nome'], 
        idade=data['idade'], 
        materia=data['materia'], 
        observacoes=data.get('observacoes', '')
    )
    db.session.add(novo_professor)
    db.session.commit()
    return jsonify({'message': 'Professor criado com sucesso'}), 201

@professor_blueprint.route('', methods=['GET'])
def listar_professores():
    professores = Professor.query.all()
    return jsonify([
        {'id': professor.id, 'nome': professor.nome, 'idade': professor.idade, 'materia': professor.materia, 'observacoes': professor.observacoes} for professor in professores
    ])

@professor_blueprint.route('/<int:id>', methods=['DELETE'])
def excluir_professor(id):
    professor = Professor.query.get(id)
    if professor:
        db.session.delete(professor)
        db.session.commit()
        return jsonify({'message': 'Professor excluído com sucesso'}), 200
    return jsonify({'error': 'Professor não encontrado'}), 404
