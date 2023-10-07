import pytest
from unittest.mock import patch, MagicMock
from app.conekta.api_wrapper import ConektaAPI

@pytest.fixture
def mock_conekta_api():
    return MagicMock(spec=ConektaAPI)

@patch('app.conekta.api_wrapper.ConektaAPI', autospec=True) 
def test_create_charge(client, mock_conekta_api, app):
    mock_conekta_api.create_charge.return_value = {
        "id": "6521185b9a90aa001a336aef",
        "livemode": False,
        "created_at": 1696667739,
        "currency": "MXN",
        "failure_code": None,
        "failure_message": None,
        "monthly_installments": None,
        "device_fingerprint": None,
        "channel": None,
        "payment_method": {
            "service_name": "OxxoPay",
            "barcode_url": "https://barcodes.conekta.com/sandbox_reference.png",
            "store": None,
            "auth_code": None,
            "object": "cash_payment",
            "type": "oxxo",
            "expires_at": 1699315200,
            "store_name": "OXXO",
            "reference": "98000017159966",
            "cashier_id": None
        },
        "object": "charge",
        "description": "Payment from order",
        "is_refundable": False,
        "reference_id": None,
        "status": "pending_payment",
        "amount": 20000,
        "paid_at": None,
        "customer_id": "",
        "order_id": "ord_2ugqzC1EREY6hcEDP",
        "refunds": None
        }
    
    # Assuming ConektaAPI is instantiated within your create_charge view
    app.view_functions['conekta_blueprint.create_charge'] = MagicMock(
        return_value=mock_conekta_api.create_charge('ord_2ugqzC1EREY6hcEDP', {})
    )
    
    response = client.post('/create_charge?ord_id=ord_2ugqzC1EREY6hcEDP', json={})
    assert response.status_code == 200
    print(response.get_json())
    assert response.get_json()['id'] == "6521185b9a90aa001a336aef"