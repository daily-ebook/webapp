import os
import uuid

from flask import Blueprint, jsonify, request, send_from_directory, url_for
from werkzeug.utils import secure_filename

upload_service = Blueprint('upload_service', __name__)
#upload_service.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024
UPLOAD_FOLDER = '/webapp/uploads'

@upload_service.route("/upload", methods=['POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({
                    'message': 'Bad Request: no file part'
                }), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({
                    'message': 'Bad Request: no selected file'
                }), 400
        if file:
            filename = secure_filename(str(uuid.uuid4()) + file.filename)
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(save_path)
            return jsonify({
                    'url': url_for('upload_service.get_file', filename=filename)
                })

@upload_service.route('/file/<filename>')
def get_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)