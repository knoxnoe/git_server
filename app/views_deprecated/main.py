from flask import Blueprint

mainapp = Blueprint('index', __name__)

@mainapp.route('/')
def index():
    return "hello world"