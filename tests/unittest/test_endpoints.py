import pytest
from unittest.mock import Mock, patch
from flask import json

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode() == 'This is a Python Flask Application wrapping the Conekta API.'

def test_create_order(client):
    mock_response = Mock()
    mock_response.json.return_value = {"id": "order_123", "status": "created"}
    
    order_data = {
        "currency": "MXN",
        "customer_info": {
            "name": "John Doe",
            "email": "john@doe.com",
            "phone": "+521234567890"
        }
    }
    
    with patch('app.conekta.ConektaAPI.create_order', return_value=mock_response.json()):
        response = client.post('/create_order', data=json.dumps(order_data), content_type='application/json')
        
    assert response.status_code == 200
    assert response.json == {"id": "order_123", "status": "created"}

def test_create_charge(client):
    mock_response = Mock()
    mock_response.json.return_value = {"id": "charge_123", "status": "success"}
    
    charge_data = {"amount": 1000, "currency": "MXN"}
    
    with patch('app.conekta.ConektaAPI.create_charge', return_value=mock_response.json()):
        response = client.post('/create_charge?ord_id=order_123', data=json.dumps(charge_data), content_type='application/json')
        
    assert response.status_code == 200
    assert response.json == {"id": "charge_123", "status": "success"}
