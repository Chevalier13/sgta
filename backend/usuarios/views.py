from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Usuario

def listar_usuarios(request):
    usuarios = list(Usuario.objects.values('id', 'nome', 'email', 'ativo'))
    return JsonResponse(usuarios, safe=False)

def buscar_usuario_por_id(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    return JsonResponse({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "ativo": usuario.ativo
    })