from flask import url_for, render_template, redirect, session, request, jsonify

import json
import os

from pydantic import BaseModel, validator, ValidationError
from typing import Optional
import re

from sqlalchemy.sql import text
from sqlalchemy.exc import DBAPIError 

from . import conekta_blueprint

from .api_wrapper import ConektaAPI

# TODO: Add a new route.

API_KEY = os.getenv('BEARER_TOKEN')

session = {"customer_info": {
        "name":"DevTest",
        "email": "test@conekta.com",
        "phone": "5522997233" }
        } 

@conekta_blueprint.route('/', methods=['GET', 'POST'])
def hello_world():
     return 'This is a Python Flask Application wrapping the Conekta API.'

@conekta_blueprint.route('/create_order', methods=['POST'])
def create_charge():
    conekta = ConektaAPI(API_KEY)
    body = request.json

    response = conekta.create_order(body)
    return jsonify(response)

@conekta_blueprint.route('/create_charge', methods=['POST'])
def create_charge():
    conekta = ConektaAPI(API_KEY)
    parameters = request.args
    body = request.json
    
    order_id = parameters.get('ord_id')

    response = conekta.create_charge(order_id, body)
    return jsonify(response)