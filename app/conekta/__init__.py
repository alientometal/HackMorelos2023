"""
The index Blueprint handles the different processes managed by the GUI.
Specifically, this Blueprint provides the different options for processes.
"""
from flask import Blueprint

conekta_blueprint = Blueprint('conekta', __name__, template_folder='templates')

from . import routes