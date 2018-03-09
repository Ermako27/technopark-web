from django.shortcuts import render


def questions(req, p=1):
    return render(req, 'questions/index.html', {
        'questions': [
            dict(id=1, title='How to fly to the moon?', desc='Rly how?', answers='100',
                 tags=['t1', 't2', 't3'],
                 author='Ermakov', rating=12),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
                 tags=['tag'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
                 tags=['tag'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
                 tags=['tag'], author='Rubinov', rating=100),
        ],
    })


# Create your views here.
def index(request):
    return render(request, 'base.html')
