# Ce fichier pourra servir à créer des utilitaire pour l'application comme des fonctions ou des enumerations
import enum

from .models import Task
from .schemas import TaskCreateModel

task_create = TaskCreateModel(
    name="Task"
    )
task_dumped = task_create.model_dump()
task = Task(**task_dumped)

