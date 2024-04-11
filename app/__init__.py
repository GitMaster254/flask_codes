from flask import Flask
from app import pages
from app.user import db



def create_app():
    app = Flask(__name__, template_folder='templates/pages')
    app = Flask(__name__, template_folder='templates')
    app.secret_key = "@secretkey#"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(pages.bp)
    db.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    
    
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
