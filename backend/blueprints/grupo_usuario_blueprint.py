from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_grupo_usuario_model import GrupoUsuarioModel
model = GrupoUsuarioModel()


grupo_usuario_blueprint = Blueprint('grupo_usuario_blueprint', __name__)


@grupo_usuario_blueprint.route('/grupo_usuario', methods=['PUT'])
@cross_origin()
def create_grupo_usuario():
    try:
        content = model.create_grupo_usuario(request.json['accesos'], request.json['restricciones'])    
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@grupo_usuario_blueprint.route('/grupo_usuario', methods=['PATCH'])
@cross_origin()
def update_grupo_usuario():
    try:
        content = model.update_grupo_usuario(request.json['id_grupo_usuario'], request.json['accesos'], request.json['restricciones'])    
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@grupo_usuario_blueprint.route('/grupo_usuario', methods=['DELETE'])
@cross_origin()
def delete_grupo_usuario():
    try:
        return jsonify(model.delete_grupo_usuario(int(request.json['id_grupo_usuario'])))
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@grupo_usuario_blueprint.route('/grupo_usuario', methods=['POST'])
@cross_origin()
def grupo_usuario():
    try:
        return jsonify(model.get_grupo_usuario(int(request.json['id_grupo_usuario'])))
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@grupo_usuario_blueprint.route('/grupo_usuarios', methods=['POST'])
@cross_origin()
def grupo_usuarios():
    try:
        return jsonify(model.get_grupo_usuarios())
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 