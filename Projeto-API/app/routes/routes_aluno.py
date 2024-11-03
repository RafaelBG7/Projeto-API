from flask import Blueprint, jsonify, request
from datetime import datetime
from ..models import Aluno, db

aluno_blueprint = Blueprint('aluno', __name__)

@aluno_blueprint.route('', methods=['POST'])
def create_aluno():
    data = request.get_json()
    try:
        data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
        novo_aluno = Aluno(
            nome=data['nome'], 
            idade=data['idade'], 
            data_nascimento=data_nascimento, 
            nota_primeiro_semestre=data['nota_primeiro_semestre'], 
            nota_segundo_semestre=data['nota_segundo_semestre'], 
            media_final=data['media_final'], 
            turma_id=data['turma_id']
        )
        db.session.add(novo_aluno)
        db.session.commit()
        return jsonify({'message': 'Aluno criado com sucesso'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@aluno_blueprint.route('', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([
        {
            'id': aluno.id,
            'nome': aluno.nome,
            'idade': aluno.idade,
            'data_nascimento': aluno.data_nascimento.isoformat(),  # Formato ISO para data
            'nota_primeiro_semestre': aluno.nota_primeiro_semestre,
            'nota_segundo_semestre': aluno.nota_segundo_semestre,
            'media_final': aluno.media_final,
            'turma_id': aluno.turma_id
        }
        for aluno in alunos
    ])
@aluno_blueprint.route('/<int:id>', methods=['DELETE'])
def excluir_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({'error': 'Aluno não encontrado'}), 404
    db.session.delete(aluno)
    db.session.commit()
    return jsonify({'message': 'Aluno excluído com sucesso'}), 200
