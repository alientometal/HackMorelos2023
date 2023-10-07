from flask import url_for, render_template, redirect, session, request, jsonify

import json

from pydantic import BaseModel, validator, ValidationError
from typing import Optional
import re

from sqlalchemy.sql import text
from sqlalchemy.exc import DBAPIError 

from . import conekta_blueprint

# TODOI: Add a new route.

@conekta_blueprint.route('/', methods=['GET', 'POST'])
def init():
    return render_template('conekta/init.html')

@conekta_blueprint.route('/connection', methods=['GET'])
def get_system_data():
    fron_info = request.args.get('data')
  

    return jsonify([])