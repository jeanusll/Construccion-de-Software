from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_secciones_model import SeccionModel
model = SeccionModel()


seccion_blueprint = Blueprint('seccion_blueprint', __name__)


@seccion_blueprint.route('/seccion', methods=['PUT'])
@cross_origin()
def create_seccion():
    try:
        content = model.create_seccion(request.json['nombre_seccion'], request.json['id_curso']) 
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@seccion_blueprint.route('/seccion', methods=['PATCH'])
@cross_origin()
def update_seccion():
    try:
        content = model.update_seccion(request.json['id_seccion'], request.json['nombre_seccion'], request.json['id_curso'])    
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@seccion_blueprint.route('/seccion', methods=['DELETE'])
@cross_origin()
def delete_seccion():
    try:
        return jsonify(model.delete_seccion(int(request.json['id_seccion'])))

    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@seccion_blueprint.route('/seccion', methods=['POST'])
@cross_origin()
def seccion():
    try:
        return jsonify(model.get_seccion(int(request.json['id_seccion'])))
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@seccion_blueprint.route('/secciones', methods=['POST'])
@cross_origin()
def secciones():
    try:
        return jsonify(model.get_secciones())
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
