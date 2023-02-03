from flask import Flask, render_template, redirect, url_for, request, session, flash
# Forms
from forms import CommentForm, ContactForm, ProjectForm, AdminForm
# Packages
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
# Controller
from controller.utils import send_message, add_project, get_projects, get_one_project, delete_one_project, admin_only
from controller.utils import get_comments, update_one_project, add_comments, delete_one_comment, delete_all_comments

from werkzeug.security import generate_password_hash
from datetime import datetime

from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)

ckeditor = CKEditor(app)
gravatar = Gravatar(app, size=50, rating='g', default='robohash',
                    force_default=False, force_lower=False, use_ssl=False, base_url=None)

app.config.from_pyfile("config.py")


@app.route('/', methods=["GET", "POST"])
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


@app.route("/add-project", methods=["GET", "POST"])
@admin_only
def create_project():
    form = ProjectForm()
    if request.method == "POST":
        add_project(form.title.data,
                    form.subtitle.data,
                    form.img_url.data,
                    form.body.data)
        return redirect(url_for("index"))
    else:
        return render_template("add-project.html", form=form)


@app.route("/project/<id>", methods=["GET", "POST"])
def show_project(id):
    form = CommentForm()
    comments = get_comments(id)
    is_active = session.get("is_active", False)
    projectID = id
    if request.method == "POST":
        name = form.name.data
        text = form.text.data
        add_comments(id=id, text=text, author=name)
        return redirect(url_for("show_project", id=id))
    else:
        return render_template("project.html", **get_one_project(id),
                               form=form,
                               comments=comments,
                               id=projectID,
                               is_active=is_active
                               )


@app.route("/delete-project/<id>")
@admin_only
def delete_project(id):
    delete_one_project(id)
    return redirect(url_for("index"))


@app.route("/edit-project/<id>", methods=["GET", "POST"])
@admin_only
def edit_project(id):
    project = get_one_project(id)
    is_edit = True
    if request.method == "POST":
        update_one_project(project,
                           request.form.get("title"),
                           request.form.get("subtitle"),
                           request.form.get("img_url"),
                           request.form.get("body")
                           )
        return redirect(url_for("index"))
    else:
        edit_form = ProjectForm(
            project.get("title"),
            project.get("subtitle"),
            project.get("img_url"),
        )
        article_body = project.get("body")  # CKeditor
        return render_template("add-project.html", form=edit_form,  article_body=article_body, is_edit=is_edit)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    form = AdminForm()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == os.getenv("KULLANICI_ADI") and password == os.getenv("PAROLA"):
            session["username"] = username
            session["password"] = generate_password_hash(password)
            session["is_active"] = True
            return redirect(url_for("index"))
        else:
            flash("Lütfen Bilgilerinizi Kontrol Ediniz..")
            return redirect(url_for("admin"))
    return render_template("admin-login.html", form=form)


@app.route("/delete-comment", methods=["GET", "POST"])
@admin_only
def delete_comment():
    id = request.form.get("projectID")
    comment = [request.args.get("text"),
               request.args.get("author"),
               request.args.get("date")]
    delete_one_comment(id, comment)
    return redirect(url_for("show_project", id=id))


@app.route("/delete-comments", methods=["GET", "POST"])
@admin_only
def delete_comments():
    id = request.form.get("projectID")
    delete_all_comments(id)
    return redirect(url_for("show_project", id=id))


@app.route("/logout")
@admin_only
def logout():
    [session.pop(key) for key in list(session.keys()) if key != '_flashes']
    return redirect(url_for("index"))


@app.context_processor
def copyright():
    return {"year": datetime.now().year}


@app.errorhandler(404)
def bad_request(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
