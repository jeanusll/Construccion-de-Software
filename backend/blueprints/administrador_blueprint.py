from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_administrador_model import AdministradorModel
model = AdministradorModel()


administrador_blueprint = Blueprint('administrador_blueprint', __name__)


@administrador_blueprint.route('/administrador', methods=['PUT'])
@cross_origin()
def create_administrador():
    try:
        content = model.create_administrador(request.json['id_usuario'])    
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 
    

@administrador_blueprint.route('/administrador', methods=['PATCH'])
@cross_origin()
def update_administrador():
    try:
        content = model.update_administrador(request.json['id_administrador'], request.json['id_usuario'])    
        return jsonify(content)        
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@administrador_blueprint.route('/administrador', methods=['DELETE'])
@cross_origin()
def delete_administrador():
    try:
        return jsonify(model.delete_administrador(int(request.json['id_administrador'])))            
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@administrador_blueprint.route('/administrador', methods=['POST'])
@cross_origin()
def administrador():
    try:
        return jsonify(model.get_administrador(int(request.json['id_administrador'])))              
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@administrador_blueprint.route('/administradores', methods=['POST'])
@cross_origin()
def administradores():
    try:
        return jsonify(model.get_administradores())    
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@administrador_blueprint.route('/profe_curso', methods=['POST'])
@cross_origin()
def profe_curso():
    try:
        return jsonify(model.profe_curso(request.json['profesor_dni'], request.json['id_curso']))    
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 
