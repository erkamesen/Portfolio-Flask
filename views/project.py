from flask import Blueprint, redirect, render_template, url_for, request, session
from controller.utils import admin_only, add_project, add_comments, get_one_project, delete_one_project
from controller.utils import update_one_project, get_comments, delete_one_comment, delete_all_comments
from forms import ProjectForm, CommentForm

project = Blueprint("project", __name__,
                    template_folder="../templates", static_folder="../static")


@project.route("/add-project", methods=["GET", "POST"])
@admin_only
def create_project():
    form = ProjectForm()
    if request.method == "POST":
        add_project(form.title.data,
                    form.subtitle.data,
                    form.img_url.data,
                    form.body.data)
        return redirect(url_for("home.index"))
    else:
        return render_template("add-project.html", form=form)


@project.route("/project/<id>", methods=["GET", "POST"])
def show_project(id):
    form = CommentForm()
    comments = get_comments(id)
    print(comments)
    is_active = session.get("is_active", False)
    projectID = id
    if request.method == "POST":
        name = form.name.data
        text = form.text.data
        add_comments(id=id, text=text, author=name)
        return redirect(url_for("project.show_project", id=id))
    else:
        return render_template("project.html", **get_one_project(id),
                               form=form,
                               comments=comments,
                               id=projectID,
                               is_active=is_active
                               )


@project.route("/delete-project/<id>")
@admin_only
def delete_project(id):
    delete_one_project(id)
    return redirect(url_for("home.index"))


@project.route("/edit-project/<id>", methods=["GET", "POST"])
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
        return redirect(url_for("home.index"))
    else:
        edit_form = ProjectForm(
            title=project.get("title"),
            subtitle=project.get("subtitle"),
            img_url=project.get("img_url"),
        )
        article_body = project.get("body")  # CKeditor
        return render_template("add-project.html", form=edit_form,  article_body=article_body, is_edit=is_edit)


@project.route("/delete-comment", methods=["GET", "POST"])
@admin_only
def delete_comment():
    id = request.form.get("projectID")
    comment = [request.args.get("text"),
               request.args.get("author"),
               request.args.get("date")]
    delete_one_comment(id, comment)
    return redirect(url_for("project.show_project", id=id))


@project.route("/delete-comments", methods=["GET", "POST"])
@admin_only
def delete_comments():
    id = request.form.get("projectID")
    delete_all_comments(id)
    return redirect(url_for("project.show_project", id=id))
