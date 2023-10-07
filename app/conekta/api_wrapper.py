import requests
import json

class ConektaAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def create_charge(self, ord_id, body):
        """
        The create_charge function creates a charge for the order.
            Args:
                ord_id (str): The id of the order to be charged.
                body (dict): A dictionary containing information about the payment method, amount and currency.
            Returns:
                dict: A dictionary containing information about the charge.
        
        Args:
            self: Represent the instance of the class
            ord_id: Create a charge for the order with the given id
            body: Pass the information of the card to be charged
        
        Returns:
            A dictionary
        """
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
        """
        The create_order function creates an order in Conekta.
            Args:
                body (dict): A dictionary containing the following keys:
                    currency (str): The currency of the order, e.g., &quot;MXN&quot;.
                    customer_info (dict): A dictionary containing the following keys:
                        name (str): The full name of your customer, e.g., &quot;John Doe&quot;.
                        email (str): Your customer's email address, e.g., &quot;john@doe.com&quot;.
                        phone(str) : Your customer's phone number with country code and
        
        Args:
            self: Represent the instance of the class
            body: Pass the data that will be used to create the order
        
        Returns:
            A dictionary with the following keys:
        """
    
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