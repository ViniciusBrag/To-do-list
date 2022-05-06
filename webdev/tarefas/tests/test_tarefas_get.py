from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertContains

@pytest.fixture
def resposta(client):
    """_summary_

    Args:
        client (_type_): Módulo de emular requisições http
        reverse (_type_): Módulo de emular requisições http
        
    """
    resp = client.get(reverse('tarefas:home'))
    return resp

def test_status_code(resposta):
    """_summary_

    Args:
        resp (_fixture_): Função que emula e reverse urls renomeadas.
        status_code (_método_): Método da função client que retorna verbos http.
    """
    assert resposta.status_code == 200


def test_formulario_presente(resposta):
    """_summary_

    Args:
        assertContains (_type_): Método da framework django que disponibiliza verificar asserções.
    """
    assertContains(resposta, '<form>')


def test_botao_salvar_presente(resposta):
    """_summary_

    Args:
        assertContains (_type_): Método da framework django que disponibiliza verificar asserções.
    """
    assertContains(resposta, '<button type="submit')    

