from django.shortcuts import render


def questions(request, p=1):
    return render(request, 'questions/index.html', {
        'questions': [
            dict(id=1, title='How to fly to the moon?', desc='Rly how?', answers='100',
                 tags=['c++', 'python', 'c#'],
                 author='Ermakov', rating=12),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
                 tags=['c++'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
                 tags=['python'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
                 tags=['c#'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
                 tags=['perl'], author='Rubinov', rating=100),
        ],
    })


def one_question_page(request, title, text):
    question = dict(id=1, title=str(title), desc=str(text), answers='100',
                                                                tags=['t1', 't2', 't3'],
                                                                author='Ermakov', rating=12)
    return render(request, 'questions/question.html', {
        'question': question,

        'comments': [
            dict(id=1, title='How to fly to the moon?', text='Call Ilon Musk', answers='100',
                 tags=['t1', 't2', 't3'],
                 author='Ermakov', rating=9, is_correct=1),
            dict(id=1, title='How to fly to the moon?', text='Smoke weed', answers='100',
                 tags=['t1', 't2', 't3'],
                 author='Rubinov', rating=3, is_correct=0),
            dict(id=1, title='How to fly to the moon?', text='Choose blue tablet', answers='100',
                 tags=['t1', 't2', 't3'],
                 author='Morozov', rating=12, is_correct=1)

        ]



    })


def tag(request, tag):
    return render(request, 'questions/tag.html', {
        'tag': str(tag),
        'questions': [
            dict(id=1, title='How to fly to the moon?', desc='Rly how?', answers='100',
                 tags=['c++', 'python', 'c#']),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
                 tags=['c#', 'python'], author='Rubinov', rating=100)
        ]


    })


def very_hot(request):
    return render(request, 'questions/hot.html', {
        'questions': [
            dict(id=1, title='How to fly to the moon?', desc='Rly how?', answers='100',
                 tags=['c++', 'python', 'c#'],
                 author='Ermakov', rating=12),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
                 tags=['c++'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
                 tags=['python'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
                 tags=['c#'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
                 tags=['perl'], author='Rubinov', rating=100),
        ],
    })


def ask(request):
    return render(request, 'questions/ask.html', {'title': 'New question'})



# Create your views here.
def index(request):
    return render(request, 'base.html', {'current_user': 1})
