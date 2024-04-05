from flask import Blueprint, render_template, request, redirect, url_for, flash, session

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

@bp.route("/signin", methods=['GET', 'POST']) # type: ignore
def signin():
     return render_template("pages/signin.html")  # Redirect to the sign-in page again
     

@bp.route("/dashboard") 
def dashboard():
    return render_template("pages/dashboard.html")
