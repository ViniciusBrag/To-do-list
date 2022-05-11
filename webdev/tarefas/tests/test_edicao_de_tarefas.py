from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertContains

from webdev.tarefas.models import Tarefa



@pytest.fixture
def tarefa_feita(db):
   return Tarefa.objects.create(nome='Tarefa ', feita=True) 


@pytest.fixture
def resposta_com_tarefas_pendentes(client, tarefas_feitas):
    resp = client.post(reverse('tarefas:detalhe', kwargs={'tarefa_id': tarefas_feitas.id}),
        data={'nome': f'{tarefas_feitas.nome}-editada'}
    )
    return resp





@pytest.fixture
def tarefas_pendentes(db):
    """_summary_
    Teste para criação de tarefas no banco de dados.

    Args:
        db (_type_): Padrão do django para acessar o banco de dados
    """
    return Tarefa.objects.create(nome='tarefa 1', feita=False)



@pytest.fixture
def resposta_com_tarefas_pendentes(client, tarefas_pendentes):
    """_summary_
    Fixture com verbo get para acessar se a resposta foi feita com a lista de Tarefas pendentes.

    Args:
        client (_type_): Módulo de emular requisições http
        reverse (_type_): Módulo de emular requisições http
        
    """
    resp = client.post(reverse('tarefas:detalhe', kwargs={'tarefa_id': tarefas_pendentes.id}),
        data={'feita': 'true', 'nome': f'{tarefas_pendentes.nome}-editada'}
    )
    return resp


def test_status_code(resposta_com_tarefas_pendentes):
    """_summary_

    Args:
        resp (_fixture_): Função que emula e reverse urls renomeadas.
        status_code (_método_): Método da função client que retorna verbos http.
    """
    assert resposta_com_tarefas_pendentes.status_code == 302

def test_tarefa_feita(resposta_com_tarefas_pendentes, db):
    assert Tarefa.objects.first().feita



