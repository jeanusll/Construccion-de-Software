from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_horario_model import HorarioModel
model = HorarioModel()


horario_blueprint = Blueprint('horario_blueprint', __name__)


@horario_blueprint.route('/horario', methods=['PUT'])
@cross_origin()
def create_horario():
    try:
        content = model.create_horario(request.json['id_curso'], request.json['hora_inicio'], request.json['hora_final'], request.json['dia'], request.json['aula']) 
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@horario_blueprint.route('/horario', methods=['PATCH'])
@cross_origin()
def update_horario():
    try:
        content = model.update_horario(request.json['id_horario'], request.json['id_curso'], request.json['hora_inicio'], request.json['hora_final'], request.json['dia'], request.json['aula'])    
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@horario_blueprint.route('/horario', methods=['DELETE'])
@cross_origin()
def delete_horario():
    try:
        return jsonify(model.delete_horario(int(request.json['id_horario'])))
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@horario_blueprint.route('/horario', methods=['POST'])
@cross_origin()
def horario():
    try:
        return jsonify(model.get_horario(int(request.json['id_horario'])))
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@horario_blueprint.route('/horarios', methods=['POST'])
@cross_origin()
def horarios():
    try:
        return jsonify(model.get_horarios())
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 
