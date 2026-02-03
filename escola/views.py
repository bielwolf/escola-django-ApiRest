from django.shortcuts import render
from django.http import JsonResponse

def estudantes(request):
    if request.method == 'GET':
        estudantes = [
            {'id': 1, 'nome': 'Ana Silva', 'idade': 20},
            {'id': 2, 'nome': 'Bruno Souza', 'idade': 22},
            {'id': 3, 'nome': 'Carla Pereira', 'idade': 19},
        ]
        return JsonResponse(estudantes, safe=False)