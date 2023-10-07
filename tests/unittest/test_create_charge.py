import pytest
from unittest.mock import MagicMock
from your_module import ConektaAPI

@pytest.fixture
def mock_conekta_api():
    mock = MagicMock(spec=ConektaAPI)
    mock.create_charge.return_value = """{
        "id": "6521185b9a90aa001a336aef",
        "livemode": false,
        "created_at": 1696667739,
        "currency": "MXN",
        "failure_code": null,
        "failure_message": null,
        "monthly_installments": null,
        "device_fingerprint": null,
        "channel": null,
        "payment_method": {
            "service_name": "OxxoPay",
            "barcode_url": "https://barcodes.conekta.com/sandbox_reference.png",
            "store": null,
            "auth_code": null,
            "object": "cash_payment",
            "type": "oxxo",
            "expires_at": 1699315200,
            "store_name": "OXXO",
            "reference": "98000017159966",
            "cashier_id": null
        },
        "object": "charge",
        "description": "Payment from order",
        "is_refundable": false,
        "reference_id": null,
        "status": "pending_payment",
        "amount": 20000,
        "paid_at": null,
        "customer_id": "",
        "order_id": "ord_2ugqzC1EREY6hcEDP",
        "refunds": null
        }"""
    return mock

def test_create_order(mock_conekta_api):
    payment_integration = ConektaAPI(mock_conekta_api)
    order_data = { "payment_method": { "type": "cash" } }
    response = payment_integration.create_order(order_data)
    
    assert 'conekta' in response
