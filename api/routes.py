from flask import Blueprint, jsonify, request

# celery tasks
from scheduler import celery
from celery.result import AsyncResult

# modules
import json

import utils

api = Blueprint('api', __name__)

@api.route("/generate", methods=['POST'])
def generate():
    recipe_json = request.form.get("recipe")
    recipe_dict = json.loads(recipe_json)
    task = celery.send_task('data_provider.generate_book_from_dict_recipe', args=[recipe_dict], kwargs={})
    return jsonify(task.id)

@api.route('/status/<task_id>')
def status(task_id):
    task = celery.AsyncResult(task_id)
    response = utils.generate_response_from_task(task)
    return jsonify(response)

@api.route('/sources')
def sources():
    task = celery.send_task('data_provider.get_sources_metadata', args=[], kwargs={})
    response = task.get()
    return jsonify(response)

@api.app_errorhandler(404)
def error404(e):
    return jsonify({ "id": "endpoint_not_found", "message": "API endpoint not found"}), 404