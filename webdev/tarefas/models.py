from django.db import models

# Create your models here.
class Tarefa(models.Model):
    """_summary_
    Classe criado no intuito de criar nova tarefas.
    Args:
        models (Método de uma classe): Método de uma classe padrão do django para criar modelos no banco de daos (ORM)
        nome (Nome da Tarefa): Campo respectivo ao nome da tarefa a ser executada.
        feita (Campo de opção): Campo destinado a opção de feito ou não a tarefa.
    """
    nome = models.CharField(max_length=128)
    feita = models.BooleanField(default=False)
