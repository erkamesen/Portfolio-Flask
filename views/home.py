from flask import Blueprint, request, session, render_template, send_file
from models import Service, Project
from forms import ContactForm
from controller.utils import send_message

home = Blueprint("home", __name__, template_folder="../templates",
                 static_folder="../static")

service_db = Service("services")
project_db = Project("projects")


@home.route('/', methods=["GET", "POST"])
def index():
    form = ContactForm()
    is_active = session.get("is_active", False)
    projects = project_db.get_projects()
    services = service_db.get_services()
    if form.validate_on_submit():
        send_message(request.form.get("name"),
                     request.form.get("email"),
                     request.form.get("subject"),
                     request.form.get("text")
                     )
        return render_template("index.html", form=form)
    else:
        return render_template('index.html', form=form,
                               projects=projects,
                               services=services,
                               is_active=is_active)



@home.route("/download-resume")
def download():
    return send_file("./resume.pdf", as_attachment=True)
