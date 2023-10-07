import json
import requests
from unittest.mock import Mock
from app.conekta.api_wrapper import ConektaAPI 

class MockResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data

def test_create_order_authentication_error():
    # Arrange
    api_key = "key_mRtflzDbQGCMAp3vMMKzv"  # invalid API key
    conekta_api = ConektaAPI(api_key)
    body = {"amount": 1000, "currency": "MXN"}

    # Simulate a 401 response (authentication error)
    mock_response = MockResponse(401, {"error": "Authentication failed"})

    # Patch the requests.post method to return the mock response
    with Mock.patch("requests.post", return_value=mock_response):
        # Act
        response = conekta_api.create_order(body)

        # Assert
        assert response == {"error": "Authentication failed"}

def test_create_order_entity_not_found():
    # Arrange
    api_key = "key_mRtflzDbQGCMAp3vMMKzvEs"  # valid API key
    conekta_api = ConektaAPI(api_key)
    body = {"amount": 1000, "currency": "MXN"}

    # Simulate a 404 response (entity not found)
    mock_response = MockResponse(404, {"error": "Entity not found"})

    # Patch the requests.post method to return the mock response
    with Mock.patch("requests.post", return_value=mock_response):
        # Act
        response = conekta_api.create_order(body)

        # Assert
        assert response == {"error": "Entity not found"}

def test_create_order_precondition_required():
    # Arrange
    api_key = "key_mRtflzDbQGCMAp3vMMKzvEs"  # valid API key
    conekta_api = ConektaAPI(api_key)
    body = {}  # Empty body to trigger precondition required error

    # Simulate a 428 response (precondition required)
    mock_response = MockResponse(428, {"error": "Precondition required"})

    # Patch the requests.post method to return the mock response
    with Mock.patch("requests.post", return_value=mock_response):
        # Act
        response = conekta_api.create_order(body)

        # Assert
        assert response == {"error": "Precondition required"}
