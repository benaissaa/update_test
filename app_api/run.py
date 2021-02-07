
from flask import Flask, request
from flask_cors import CORS
from flask import Blueprint

def create_app(config_filename=None):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    CORS(app)
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='')

    from Model.db import db
    db.init_app(app)
    
    

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)