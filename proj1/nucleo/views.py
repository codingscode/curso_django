from django.shortcuts import render


def index(request):
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


    context = {
        'curso': 'Prog Django', 'outro': 'javascript', 'logado': teste
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')







