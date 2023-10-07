import requests
import json

class ConektaAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def create_charge(self, ord_id, body):
        headers = {
            "accept": "application/vnd.conekta-v2.1.0+json",
            "Accept-Language": "es",
            "content-type": "application/json",
            "authorization": f"Bearer {self.api_key}"
        }
        response = requests.post(
            f'https://api.conekta.io/orders/{ord_id}/charges',
            headers=headers,
            data=json.dumps(body)
        )
        return response.json()

    def create_order(self, body):
    
        headers = {
            "accept": "application/vnd.conekta-v2.1.0+json",
            "Accept-Language": "es",
            "content-type": "application/json",
            "authorization": f"Bearer {self.api_key}"
        }
        response = requests.post(
            "https://api.conekta.io/orders",
            headers=headers,
            data=json.dumps(body)
        )
        return response.json()