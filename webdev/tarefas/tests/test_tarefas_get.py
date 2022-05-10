from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertContains

from webdev.tarefas.models import Tarefa

@pytest.fixture
def resposta(client, db):
    """_summary_
    Fixture criada para fazer um get em busca de informações na aplicação

    Args:
        client (_type_): Módulo de emular requisições http
        reverse (_type_): Módulo de emular requisições http
        db (_type__) : Padrão do django para acessar o banco de dados
        
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
    Teste para verificação do formulário presente no template.

    Args:
        assertContains (_type_): Método da framework django que disponibiliza verificar asserções.
    """
    assertContains(resposta, '<form')


def test_botao_salvar_presente(resposta):
    """_summary_
    Teste para verificação do botão salvar se está presente no template.

    Args:
        assertContains (_type_): Método da framework django que disponibiliza verificar asserções.
    """
    assertContains(resposta, '<button type="submit')    



@pytest.fixture
def lista_de_tarefas_pendentes(db):
    """_summary_
    Teste para criação de tarefas no banco de dados.

    Args:
        db (_type_): Padrão do django para acessar o banco de dados
    """
    tarefas =[ 
        Tarefa(nome='tarefa 1', feita=False),
        Tarefa(nome='tarefa 2', feita=False),
    ]
    Tarefa.objects.bulk_create(tarefas)
    return tarefas


@pytest.fixture
def resposta_com_lista_de_tarefas(client, lista_de_tarefas_pendentes):
    """_summary_
    Fixture com verbo get para acessar se a resposta foi feita com a lista de Tarefas pendentes.

    Args:
        client (_type_): Módulo de emular requisições http
        reverse (_type_): Módulo de emular requisições http
        
    """
    resp = client.get(reverse('tarefas:home'))
    return resp


def test_lista_de_tarefas_pendentes_present(resposta_com_lista_de_tarefas, lista_de_tarefas_pendentes):
    """_summary_
    Teste com verbo get para listar tarefas que estão com a objeto "feita=False" no banco de dados


    Args:
        assertContains (_type_): Método da framework django que disponibiliza verificar asserções.
    """
    for tarefa in lista_de_tarefas_pendentes:
        assertContains(resposta_com_lista_de_tarefas, tarefa.nome)  