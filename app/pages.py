from flask import Blueprint, render_template

#creating instance with pages(the name of the blueprint)
bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route("/services")
def services():
    return render_template("pages/services.html")