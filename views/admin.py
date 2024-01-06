from flask import Blueprint, request, session, redirect, url_for, flash, render_template
from forms import AdminForm
from controller.utils import admin_only
from werkzeug.security import generate_password_hash

from dotenv import load_dotenv
import os

load_dotenv()


admin = Blueprint("admin", __name__,
                  template_folder="../templates", static_folder="../static")


@admin.route("/admin", methods=["GET", "POST"])
def admin_login():
    form = AdminForm()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == os.getenv("USERNAME") and password == os.getenv("PASSWORD"):
            session["username"] = username
            session["password"] = generate_password_hash(password)
            session["is_active"] = True
            return redirect(url_for("home.index"))
        else:
            flash("Incorrect username or password.")
            return redirect(url_for("home.index"))
    return render_template("admin-login.html", form=form)


@admin.route("/logout-admin")
@admin_only
def logout():
    [session.pop(key) for key in list(session.keys()) if key != '_flashes']
    return redirect(url_for("home.index"))
