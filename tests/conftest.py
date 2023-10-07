import pytest
from app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here
@pytest.fixture(scope='module')
def test_client():
    # Create a Flask app configured for testing
    flask_app = create_app()
    flask_app.config.from_object('config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

@pytest.fixture()
def client_with_new_ingestion_session(client):
    with client.session_transaction() as sess:
        sess["EDL_PROCESS"] = "New Ingestion"
    return client

@pytest.fixture()
def client_with_new_outbound_session(client):
    with client.session_transaction() as sess:
        sess["EDL_PROCESS"] = "New Outbound"
    return client