from flask import Flask, jsonify, json
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from sqlalchemy.orm import sessionmaker
from werkzeug.routing import BaseConverter
import decimal
from config import load_config
from flask_login import LoginManager
ApplicationConfig = load_config()



app = Flask(__name__)
app.config.from_object(ApplicationConfig)
session = sessionmaker()

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

UPLOADED_FILES_DEST_USER = ApplicationConfig.UPLOADED_FILES_DEST_USER
UPLOADED_FILES_DEST_ITEM = ApplicationConfig.UPLOADED_FILES_DEST_ITEM
UPLOADED_FILES_ALLOW = ApplicationConfig.UPLOADED_FILES_ALLOW

app.config['UPLOADED_FILES_DEST_USER'] = ApplicationConfig.UPLOADED_FILES_DEST_USER
app.config['UPLOADED_FILES_DEST_ITEM'] = ApplicationConfig.UPLOADED_FILES_DEST_ITEM
app.config['UPLOADED_FILES_ALLOW'] = ApplicationConfig.UPLOADED_FILES_ALLOW
app.url_map.converters['regex'] = RegexConverter
app.json_encoder = DecimalEncoder


session.configure(bind=ApplicationConfig.SQLALCHEMY_DATABASE_URI)
db = SQLAlchemy(app)
server_session = Session(app)
ma = Marshmallow(app)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.anonymous_user = "Guest"



@app.errorhandler(500)
def internal_error500():
    return jsonify({"error": "Internal Error 500"}), 500


@app.errorhandler(502)
def internal_error502(error):
    return jsonify({"error": "Internal Error 502"}), 502


@app.errorhandler(404)
def internal_error404(error):
    return jsonify({"error": "Internal Error 400"}), 400


@app.errorhandler(401)
def internal_error404(error):
    return jsonify({"error": "Internal Error 401"}), 401


@app.errorhandler(400)
def internal_error400(error):
    return jsonify({"error": "Internal Error 400"}), 400


@app.errorhandler(413)
def to_large_file(error):
    return jsonify({"error": "File is too large.  Use a smaller image/file."}), 413


@app.errorhandler(403)
def internal_error403(error):
    return jsonify({"error": "Internal Error 403"}), 403


@app.errorhandler(405)
def internal_error(error):
    return jsonify({"error": "Internal Error 405"}), 405

# link locations
from .main import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/main')


