from flask import Blueprint


bp = Blueprint('auth', __name__)

from blog.auth import routes