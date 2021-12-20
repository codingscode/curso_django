from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from django.template import loader


from .models import Produto


def index(request):
    """
    print(dir(request))
    print(f'metodo: {request.method}')
    print(f'Headers: {request.headers}')
    print(f'headers user-agent: {request.headers["User-Agent"]}')
    print(f'User: {request.user}')
    print(f"request.user: {dir(request.user)}")


    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        print(f"request.user.last_name: {request.user.last_name}")  # testar request.user.email
        teste = 'Usuário logado'
    """

    produtos = Produto.objects.all()
    

    context = {
        'curso': 'Prog Django',
        'outro': 'javascript',
        # 'logado': teste
        'produtos': produtos
        
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    print(f'PK: {pk}')
    #prod = Produto.objects.get(id=pk)
    
    prod = get_object_or_404(Produto, id=pk)
    
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)













