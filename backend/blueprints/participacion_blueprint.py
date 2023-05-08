from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_participacion_model import ParticipacionModel

participacion_model = ParticipacionModel()

participacion_blueprint = Blueprint('participacion_blueprint', __name__)

@participacion_blueprint.route('/participacion', methods=['PUT'])
@cross_origin()
def create_participacion():
    content = participacion_model.create_participacion(request.json['dni_alumno'], request.json['id_curso'], request.json['total_puntos'])    
    return jsonify(content)

@participacion_blueprint.route('/participacion', methods=['PATCH'])
@cross_origin()
def update_participacion():
    content = participacion_model.update_participacion(request.json['id_participacion'], request.json['dni_alumno'], request.json['id_curso'], request.json['total_puntos'])    
    return jsonify(content)

@participacion_blueprint.route('/participacion', methods=['DELETE'])
@cross_origin()
def delete_participacion():
    return jsonify(participacion_model.delete_participacion(request.json['id_participacion']))

@participacion_blueprint.route('/participacion', methods=['POST'])
@cross_origin()
def get_participacion():
    return jsonify(participacion_model.get_participacion(request.json['id_participacion']))

@participacion_blueprint.route('/participaciones', methods=['POST'])
@cross_origin()
def get_participaciones():
    return jsonify(participacion_model.get_participaciones())
