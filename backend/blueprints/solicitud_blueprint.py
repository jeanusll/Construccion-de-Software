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
    content = solicitud_model.create_solicitud(request.json['id_asistencia'], request.json['documento'], request.json['justificacion'])    
    return jsonify(content)

@solicitud_blueprint.route('/solicitud', methods=['PATCH'])
@cross_origin()
def update_solicitud():
    content = solicitud_model.update_solicitud(request.json['id_solicitud'], request.json['id_asistencia'], request.json['documento'], request.json['justificacion'])    
    return jsonify(content)

@solicitud_blueprint.route('/solicitud', methods=['DELETE'])
@cross_origin()
def delete_solicitud():
    return jsonify(solicitud_model.delete_solicitud(request.json['id_solicitud']))

@solicitud_blueprint.route('/solicitud', methods=['POST'])
@cross_origin()
def solicitud():
    return jsonify(solicitud_model.get_solicitud(request.json['id_solicitud']))

@solicitud_blueprint.route('/solicitudes', methods=['POST'])
@cross_origin()
def solicitudes():
    return jsonify(solicitud_model.get_solicitudes())
