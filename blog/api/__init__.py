from flask import Blueprint


bp = Blueprint('api', __name__)

from blog.api import users, errors, tokens
