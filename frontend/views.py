import flask

frontend = flask.Blueprint('frontend', __name__,
    template_folder="./templates/",
    static_folder="./static/",
    static_url_path="/static/frontend")

@frontend.route("/")
def index():
    return flask.render_template("home.html")

@frontend.route("/sources")
def list_sources():
    return flask.render_template("list-sources.html")

@frontend.route("/create-recipe")
def create_recipe():
    return flask.render_template("create-recipe.html")

@frontend.route("/status/<task_id>")
def show_status(task_id):
    return flask.render_template("show-status.html", task_id=task_id)
        
# this allow us to build a fake static js file which has all the route configured,
# this is done since we can't use url_for in static js files
@frontend.route(frontend.static_url_path + "/js/routes.js")
def js_routes():
    resp = flask.Response(response=flask.render_template("js/routes.js"),
        status=200, \
        mimetype="text/javascript")
    return resp
