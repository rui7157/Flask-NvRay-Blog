from flask import Blueprint

main = Blueprint("view", __name__)

from . import nav
