from django.urls import reverse
import pytest
from webdev.tarefas.models import Tarefa


@pytest.fixture
def tarefa(db):
    """_summary_
    Teste para criação de tarefas no banco de dados.

    Args:
        db (_type_): Padrão do django para acessar o banco de dados
    """
    return Tarefa.objects.create(nome='tarefa 1', feita=False)



@pytest.fixture
def resposta(client, tarefa):
    """_summary_
    Fixture com verbo get para acessar se a resposta foi feita com a lista de Tarefas pendentes.

    Args:
        client (_type_): Módulo de emular requisições http
        reverse (_type_): Módulo de emular requisições http
        
    """
    resp = client.post(reverse('tarefas:apagar', kwargs={'tarefa_id': tarefa.id}),
    )
    return resp


def test_apagar_tarefa(resposta):
    assert not Tarefa.objects.exists()