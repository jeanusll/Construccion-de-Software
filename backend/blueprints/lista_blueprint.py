from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_lista_model import ListaModel
lista_model = ListaModel()

lista_blueprint = Blueprint('lista_blueprint', __name__)

@lista_blueprint.route('/lista', methods=['POST'])
@cross_origin()
def create_lista():
    try:
        content = lista_model.create_lista(request.json['id_curso'], request.json['dni_alumno'], request.json['estado'])
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@lista_blueprint.route('/lista', methods=['PATCH'])
@cross_origin()
def update_lista():
    try:
        content = lista_model.update_lista(request.json['id_lista'], request.json['id_curso'], request.json['dni_alumno'], request.json['estado'])
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@lista_blueprint.route('/lista', methods=['DELETE'])
@cross_origin()
def delete_lista():
    try:
        return jsonify(lista_model.delete_lista(request.json['id_lista']))
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@lista_blueprint.route('/lista', methods=['POST'])
@cross_origin()
def get_lista():
    try:
        return jsonify(lista_model.get_lista(request.json['id_lista']))
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@lista_blueprint.route('/listas', methods=['POST'])
@cross_origin()
def get_listas():
    try:
        return jsonify(lista_model.get_listas())
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
