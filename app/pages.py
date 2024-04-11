from flask import Blueprint, render_template, request, redirect, session, url_for

from app.user import User
from app.user import db
 

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
    
@bp.route('/', methods=['GET', 'POST'])
def index():
    if 'user_id' in session:
        # User is already logged in, redirect to main page or profile
        return redirect(url_for('dashboard'))  # Adjust this route as needed
    else:
        # First-time visitor, redirect to sign-up page
        return redirect(url_for('signin'))

@bp.route('/signin', methods=['GET', 'POST'])    
def signin():
    error_message = None
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if username or email already exists in the database
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()

        if existing_user:
            # User or email already exists, show error message
            error_message = "Username or email already exists. Please choose a different one."
        else:
                    # Create new user
            new_user = User()
            new_user.username = username
            new_user.email = email
            new_user.set_password(password)  # Set password securely
            db.session.add(new_user)
            db.session.commit()

                    # Log in the user by storing user_id in session
            session['user_id'] = new_user.id

                    # Redirect to main page or profile
            return redirect(url_for('dashboard')) 
        
    return render_template('pages/signin.html',error_message=error_message)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists in the database
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            # User exists and password is correct, log in the user
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))  # Adjust this route as needed
        else:
            # User does not exist or password is incorrect, show error message
            error_message = "Invalid username or password"
            return render_template('login.html', error_message=error_message)

    # If request method is GET (initial page load), render the login form
    return render_template('pages/login.html')

def main_page():
    # Check if user is logged in
    if 'user_id' not in session:
        # User is not logged in, redirect to login page
        return redirect(url_for('login'))

    # User is logged in, render the main page
    return render_template('pages/dashboard.html')


