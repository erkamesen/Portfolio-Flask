from flask import Blueprint, request, session, render_template
from controller.utils import send_message, get_projects
from forms import ContactForm

home = Blueprint("home", __name__, template_folder="../templates",
                 static_folder="../static")


@home.route('/', methods=["GET", "POST"])
def index():
    form = ContactForm()
    is_active = session.get("is_active", False)
    projects = get_projects()
    if form.validate_on_submit():
        send_message(request.form.get("name"),
                     request.form.get("email"),
                     request.form.get("subject"),
                     request.form.get("text")
                     )
        return render_template("index.html", form=form)
    else:
        return render_template('index.html',    form=form,
                               projects=projects,
                               is_active=is_active)
