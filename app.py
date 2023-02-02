from flask import Flask, render_template, redirect, url_for, request
#Forms
from forms import CommentForm, ContactForm, ProjectForm, AdminForm
#Packages
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
#Controller
from controller.utils import send_message, add_project, get_projects, get_one_project, delete_one_project
from controller.utils import get_comments, update_one_project, add_comments
from werkzeug.security import check_password_hash



app = Flask(__name__)

ckeditor = CKEditor(app)
gravatar = Gravatar(app, size=50, rating='g', default='robohash',
                    force_default=False, force_lower=False, use_ssl=False, base_url=None)

app.config.from_pyfile("config.py")



@app.route('/', methods=["GET", "POST"])
def index():
    form = ContactForm()

    if form.validate_on_submit():
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        text = request.form.get("text")
        send_message(name=name, email=email, subject=subject, text=text)
        return render_template("index.html", form=form)
    else:
        projects = get_projects()
        return render_template('index.html', form=form, projects=projects)


@app.route("/add-project", methods=["GET", "POST"])
def create_project():
    form = ProjectForm()
    if request.method == "POST":
        title = form.title.data
        subtitle = form.subtitle.data
        img_url = form.img_url.data
        body = form.body.data
        add_project(title=title, subtitle=subtitle, url=img_url, body=body)
        return redirect(url_for("index"))
    return render_template("add-project.html", form=form)


@app.route("/project/<id>", methods=["GET", "POST"])
def show_project(id):
    form = CommentForm()
    data = get_one_project(id)
    comments = get_comments(id)
    if request.method == "POST":
        name = form.name.data
        text = form.text.data
        add_comments(id=id, text=text, author=name)
        return redirect(url_for("show_project", id=id))
    project = {
        "title": data.get("title"),
        "subtitle": data.get("subtitle"),
        "body": data.get("body")
    }
    return render_template("project.html", **project, form=form, comments=comments)


@app.route("/delete-project/<id>")
def delete_project(id):
    delete_one_project(id)
    return redirect(url_for("index"))


@app.route("/edit-project/<id>", methods=["GET", "POST"])
def edit_project(id):
    project = get_one_project(id)
    is_edit = True
    if request.method == "POST":
        update_one_project(project=project,
                           title=request.form.get("title"),
                           subtitle=request.form.get("subtitle"),
                           url=request.form.get("img_url"),
                           body=request.form.get("body")
                           )
        return redirect(url_for("index"))
    else:
        edit_form = ProjectForm(
            title=project.get("title"),
            subtitle=project.get("subtitle"),
            img_url=project.get("img_url"),
        )
        article_body = project.get("body")
        print(article_body)
        return render_template("add-project.html", form=edit_form,  article_body=article_body, is_edit=is_edit)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    form = AdminForm()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        pass
        
    return render_template("admin-login.html", form=form)


@app.route("/logout")
def logout():
    return redirect(url_for("index"))

@app.errorhandler(404)
def bad_request(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
