from flask import Blueprint, jsonify, request

# celery tasks
from scheduler import celery
from celery.result import AsyncResult

# modules
import json

api = Blueprint('api', __name__)

@api.route("/hello-sync")
def hello_sync():
    task = celery.send_task('tasks.print_hello')
    response = task.get()
    return jsonify(response)

@api.route("/hello")
def hello():
    task = celery.send_task('tasks.print_hello')
    return task.id

@api.route("/generate", methods=['POST'])
def generate():
    recipe_txt = request.form.get("recipe")
    recipe = json.loads(recipe_txt)
    recipe = utils.clean_recipe(recipe)
    task = celery.send_task('tasks.generate_book_from_recipe', args=[recipe], kwargs={})
    return jsonify(task.id)

@api.route('/status/<task_id>')
def status(task_id):
    task = celery.AsyncResult(task_id)
    response = generate_response_from_task(task)
    return jsonify(response)

@api.route('/sources')
def sources():
    task = celery.send_task('tasks.get_sources_metadata')
    response = task.get()
    return jsonify(response)

@api.app_errorhandler(404)
def error404(e):
    return jsonify({ "id": "endpoint_not_found", "message": "API endpoint not found"}), 404

def generate_response_from_task(task):
    response = {}
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'message': 'Pending...'
        }
    elif task.state == 'FAILURE':
        response = {
            'state': task.state,
            'message': str(task.info),    # this is the exception raised
        }
    else: 
        response = {
            'state': task.state,
            'message': task.info.get('message', '')
        }
    return response