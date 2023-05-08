from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 
from werkzeug.exceptions import BadRequest, InternalServerError


from backend.models.mysql_usuario_model import UsuarioModel
model = UsuarioModel()


usuario_blueprint = Blueprint('usuario_blueprint', __name__)

@usuario_blueprint.route('/usuario', methods=['PUT'])
@cross_origin()
def create_usuario():
    try:
        content = model.create_usuario(request.json['id_grupo_usuario'], request.json['email'], request.json['contra'])    
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f"Campo '{str(e)}' no encontrado en la petición"}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@usuario_blueprint.route('/usuario', methods=['PATCH'])
@cross_origin()
def update_usuario():
    try:
        content = model.update_usuario(request.json['id_usuario'], request.json['id_grupo_usuario'], request.json['email'], request.json['contra_anterior'],request.json['contra_nueva'] )    
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f"Campo '{str(e)}' no encontrado en la petición"}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@usuario_blueprint.route('/usuario', methods=['DELETE'])
@cross_origin()
def delete_usuario():
    try:
        return jsonify(model.delete_usuario(int(request.json['id_usuario'])))
    except KeyError as e:
        return jsonify({'Error': f"Campo '{str(e)}' no encontrado en la petición"}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@usuario_blueprint.route('/usuario', methods=['POST'])
@cross_origin()
def usuario():
    try:
        return jsonify(model.get_usuario(int(request.json['id_usuario'])))
    except KeyError as e:
        return jsonify({'Error': f"Campo '{str(e)}' no encontrado en la petición"}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@usuario_blueprint.route('/usuarios', methods=['POST'])
@cross_origin()
def usuarios():
    try:
        return jsonify(model.get_usuarios())
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 


@usuario_blueprint.route('/usuario/iniciar_sesion', methods=['POST'])
@cross_origin()
def iniciar_sesion():
    try:
        return jsonify(model.iniciar_sesion(request.json['email'], request.json['contra']))
    except KeyError as e:
        return jsonify({'Error': f"Campo '{str(e)}' no encontrado en la petición"}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500