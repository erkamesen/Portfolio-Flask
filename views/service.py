from flask import Blueprint, render_template, request, redirect, url_for
from forms import ServiceForm
from models import Service
from controller.utils import admin_only


service = Blueprint("service", __name__,
                    template_folder="../templates", static_folder="../static")

db = Service(collection="services")


@service.route("/add-service", methods=["GET", "POST"])
@admin_only
def add_service():
    form = ServiceForm()
    if form.validate_on_submit():
        db.add_service(form.title.data,
                       form.description.data,
                       form.img_url.data)
        return redirect(url_for('home.index'))
    return render_template("add-service.html", form=form)


@service.route("/edit-service/<id>", methods=["GET", "POST"])
@admin_only
def edit_service(id):
    is_edit = True
    service = db.get_service(id)
    if request.method == "POST":
        db.update_service(id,
                          request.form.get("title"),
                          request.form.get("description"),
                          request.form.get("img_url")
                          )
        return redirect(url_for("home.index"))
    else:
        edit_form = ServiceForm(
                                title=service["title"],
                                description=service["description"],
                                img_url=service["img_url"]
                                )
        return render_template("add-service.html", form=edit_form, is_edit=is_edit)



@service.route("/delete-service/<id>", methods=["GET", "POST"])
@admin_only
def delete_service(id):
    db.delete_service(id)
    return redirect(url_for("home.index"))


"""sumary_line
Python Geliştirme

Python günümüzün en popüler dillerinden olup nesne yönelimli, yüksek seviye bir programlama dilidir.
Veri analizinden web uygulamalarına kadar bir çok alanda performansı oldukça iyi olan python programlama dilinde kendini geliştiren biri olarak
 fikirlerinizi veya hayallerinizi dijital dünya da kodlara dönüştürmeniz de size yardımcı olabilirim. 
"""
