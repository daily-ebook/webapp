# flask stuff
from flask import Flask


# my blueprints
from api import api
from frontend import frontend

from scheduler import celery

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='(%',
        block_end_string='%)',
        variable_start_string='((',
        variable_end_string='))',
        comment_start_string='(#',
        comment_end_string='#)',
    ))

"""
from celerybeatmongo.models import PeriodicTask
@app.route('/enqueue')
def enqueue():
    periodic_task = PeriodicTask()
    periodic_task.name = str(uuid.uuid4())
    periodic_task.task = "tasks.print_hello"
    periodic_task.enabled = True
    interval = PeriodicTask.Interval()
    interval.every = 10
    interval.period = "seconds"

    periodic_task.interval = interval
    periodic_task.save()
    return "Enqueued"""

if __name__ == "__main__":
    app = CustomFlask(__name__)

    app.register_blueprint(frontend)
    app.register_blueprint(api, url_prefix='/api/v1')

    app.run(debug=True)
