from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_curso_model import CursoModel
model = CursoModel()


curso_blueprint = Blueprint('curso_blueprint', __name__)


@curso_blueprint.route('/curso', methods=['PUT'])
@cross_origin()
def create_curso():
    try:
        content = model.create_curso(request.json['nombre_curso'], request.json['semestre'], request.json['horas_academicas'])    
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@curso_blueprint.route('/curso', methods=['PATCH'])
@cross_origin()
def update_curso():
    try:
        content = model.update_curso(request.json['id_curso'], request.json['nombre_curso'], request.json['semestre'], request.json['horas_academicas'])    
        return jsonify(content)        
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@curso_blueprint.route('/curso', methods=['DELETE'])
@cross_origin()
def delete_curso():
    try:
        return jsonify(model.delete_curso(int(request.json['id_curso'])))
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@curso_blueprint.route('/curso', methods=['POST'])
@cross_origin()
def curso():
    try:
        return jsonify(model.get_curso(int(request.json['id_curso'])))
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@curso_blueprint.route('/cursos', methods=['POST'])
@cross_origin()
def cursos():
    try:
        return jsonify(model.get_cursos())    
    except Exception as e:
        return jsonify({'Error': str(e)}), 500    
