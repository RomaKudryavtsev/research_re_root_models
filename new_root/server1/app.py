import os

from flask import Flask, jsonify 

from new_root.models.database import db_session, init_db

from dotenv import load_dotenv

from new_root.models.models import User

load_dotenv()

app = Flask(__name__)

def create_app():
    print("Inside create_app")
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgre@localhost:5432/root_models'
    return app

@app.route('/')
def get_user():
    user = db_session.get_one(User, 1)
    return f"Hello, {user.first_name} from Server1"

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        init_db()
    app.run(port=int(os.environ.get("FLASK_RUN_PORT", 5000)))
