from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 


from backend.models.mysql_solicitud_model import SolicitudModel
solicitud_model = SolicitudModel()

solicitud_blueprint = Blueprint('solicitud_blueprint', __name__)


@solicitud_blueprint.route('/solicitud', methods=['PUT'])
@cross_origin()
def create_solicitud():
    try:
        content = solicitud_model.create_solicitud(request.json['id_asistencia'], request.json['documento'], request.json['justificacion'])    
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo requerido: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@solicitud_blueprint.route('/solicitud', methods=['PATCH'])
@cross_origin()
def update_solicitud():
    try:
        content = solicitud_model.update_solicitud(request.json['id_solicitud'], request.json['id_asistencia'], request.json['documento'], request.json['justificacion'])    
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo requerido: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@solicitud_blueprint.route('/solicitud', methods=['DELETE'])
@cross_origin()
def delete_solicitud():
    try:
        return jsonify(solicitud_model.delete_solicitud(request.json['id_solicitud']))
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@solicitud_blueprint.route('/solicitud', methods=['POST'])
@cross_origin()
def solicitud():
    try:
        return jsonify(solicitud_model.get_solicitud(request.json['id_solicitud']))
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo requerido: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@solicitud_blueprint.route('/solicitudes', methods=['POST'])
@cross_origin()
def solicitudes():
    try:
        return jsonify(solicitud_model.get_solicitudes())
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 
