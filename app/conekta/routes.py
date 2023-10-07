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
def hello_world():
     return 'This is a Python Flask Application'

@conekta_blueprint.route('/connection', methods=['GET'])
def get_system_data():
    fron_info = request.args.get('data')

# This is an example of how to get data from the frontend
@conekta_blueprint.route('/create_payment', methods=['POST'])
def create_payment():
    data = request.json
    amount = data.get('amount')
    currency = data.get('currency')
    payment_response = payment_integration.create_payment(amount, currency)
    return jsonify(payment_response)

@app.route('/create_order', methods=['POST'])
def create_order():
    order_data = request.json
    payment_response = ConektaAPI.create_order(order_data)
    return jsonify(payment_response)
  

    return jsonify([])