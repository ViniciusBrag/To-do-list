from django.test import Client
from django.urls import reverse
import pytest
from webdev.tarefas.models import Tarefa


@pytest.fixture
def resposta(client, db):
    
    """_summary_

    Args:
        client (_type_): Módulo de emular requisições http
        reverse (_type_): Módulo de emular requisições http
        db (_type__) = Fixture db para acessar o banco de dados
    """
    resp = client.post(reverse('tarefas:home'), data={'nome': 'Tarefa'})
    return resp

@pytest.fixture
def resposta_dado_invalido(client, db):
    """_summary_

  
    Args:
        client (_type_): Módulo de emular requisições http
        reverse (_type_): Módulo de emular requisições http
        db (_type__) = Fixture db para acessar o banco de dados

    Returns:
        resp_: Resposta com informações invalidas
    """
    resp = client.post(reverse('tarefas:home'), data={'nome': ''})
    return resp


def test_tarefa_existe_no_banco_de_dados(resposta):
    """_summary_
    Teste para verificação de existência de dados válidos no banco de dados.
    Args:
        resp (_fixture_): Função que emula e reverse urls renomeadas.
        status_code (_método_): Método da função client que retorna verbos http.
    """
    assert Tarefa.objects.exists()


def test_rediricionamento_depois_do_salvamento(resposta):
    """_summary_
        Teste de verificação de rediricionamento de página depois do post.
    Args:

    """
    assert resposta.status_code == 302


def test_tarefa_nao_existe_no_banco_de_dados(resposta_dado_invalido):
    """_summary_
        Teste para verificar que não existe dados invalido no banco de dados.

    Args:
        resposta_dado_invalido (fixture): Fixture paara emular dados invalidos no banco de dados.
    """
    assert not Tarefa.objects.exists()



def test_com_pagina_com_dados_invalidos(resposta_dado_invalido):
    """_summary_
        Teste de verificação de rediricionamento de página depois do post.
    Args:

    """
    assert resposta_dado_invalido.status_code == 400 

