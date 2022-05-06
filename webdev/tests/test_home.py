from django.test import Client
import pytest


@pytest.fixture
def client_code(client):
    """_summary_

    Args:
        client (_type_): Forma de emular requisições http
    """
    return client.get('/')

def test_home_status_code(client_code):
    assert client_code.status_code == 200

