from django.urls import path
from .views import (
    listar_tarefas,
    listar_tarefas_abertas,
    buscar_tarefa_por_id,
    tarefas_abertas_urgentes,
    tarefas_atrasadas,
    buscar_tarefas_por_titulo
)

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('abertas/', listar_tarefas_abertas),
    path('<int:id>/', buscar_tarefa_por_id),
    path('urgentes/', tarefas_abertas_urgentes),
    path('atrasadas/', tarefas_atrasadas),
    path('busca/<str:palavra>/', buscar_tarefas_por_titulo),
    path('<int:id>/', buscar_tarefa_por_id),

]