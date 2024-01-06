from flask import Flask, render_template

from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar

# Blueprint
from views import admin, home, project, service

from datetime import datetime

app = Flask(__name__)

ckeditor = CKEditor(app)
gravatar = Gravatar(app, size=50, rating='g', default='robohash',
                    force_default=False, force_lower=False, use_ssl=False, base_url=None)

app.config.from_pyfile("config.py")

app.register_blueprint(home)
app.register_blueprint(project)
app.register_blueprint(admin)
app.register_blueprint(service)

@app.context_processor
def copyright():
    return {"year": datetime.now().year}


@app.errorhandler(404)
def bad_request(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(port=8080)