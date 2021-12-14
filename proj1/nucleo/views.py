from django.shortcuts import render


def index(request):
    print(dir(request))

    context = {
        'curso': 'Prog Django', 'outro': 'javascript'
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')









