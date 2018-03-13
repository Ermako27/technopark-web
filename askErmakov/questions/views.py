from django.shortcuts import render
from django.core.paginator import Paginator


def _paginate(object_list, request):
    page = Paginator(object_list, 3)
    return page


def questions(request, page_number=1):

    object_list = [
            dict(id=1, title='How to fly to the moon?', desc='Rly how?', answers='100',
                 tags=['c++', 'python', 'c#'],
                 author='Ermakov', rating=12),
            dict(id=1, title='hash code slayer 1', desc='why so easy?', answers='999',
                 tags=['c++'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer 2', desc='why so easy?', answers='999',
                 tags=['python'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer 3', desc='why so easy?', answers='999',
                 tags=['c#'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer 4', desc='why so easy?', answers='999',
                 tags=['perl'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer 5', desc='why so easy?', answers='999',
                 tags=['perl'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer 6', desc='why so easy?', answers='999',
                 tags=['perl'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer 7', desc='why so easy?', answers='999',
                 tags=['perl'], author='Rubinov', rating=100),
            dict(id=1, title='hash code slayer 8', desc='why so easy?', answers='999',
                 tags=['perl'], author='Rubinov', rating=100),
        ]

    current_page = _paginate(object_list, request)

    return render(request, 'questions/index.html', {
        'questions': current_page.page(page_number)
    })


def one_question_page(request, page_number=1):
    question = dict(id=1, title='How to fly to the moon?', desc='Rly how?', answers='100',
                                                                tags=['t1', 't2', 't3'],
                                                                author='Ermakov', rating=12)

    object_list = [
            dict(id=1, title='How to fly to the moon?', text='Call Ilon Musk 1', answers='100',
                 tags=['t1', 't2', 't3'],
                 author='Ermakov', rating=9, is_correct=1),
            dict(id=1, title='How to fly to the moon?', text='Smoke weed 1', answers='100',
                 tags=['t1', 't2', 't3'],
                 author='Rubinov', rating=3, is_correct=0),
            dict(id=1, title='How to fly to the moon?', text='Choose blue tablet 1', answers='100',
                 tags=['t1', 't2', 't3'],
                 author='Morozov', rating=12, is_correct=1),
            dict(id=1, title='How to fly to the moon?', text='Call Ilon Musk 2', answers='100',
                 tags=['t1', 't2', 't3'],
                 author='Ermakov', rating=9, is_correct=1),
            dict(id=1, title='How to fly to the moon?', text='Smoke weed 2', answers='100',
                 tags=['t1', 't2', 't3'],
                 author='Rubinov', rating=3, is_correct=0),
            dict(id=1, title='How to fly to the moon?', text='Choose blue tablet 2', answers='100',
                 tags=['t1', 't2', 't3'],
                 author='Morozov', rating=12, is_correct=1),
            dict(id=1, title='How to fly to the moon?', text='Call Ilon Musk 3', answers='100',
                 tags=['t1', 't2', 't3'],
                 author='Ermakov', rating=9, is_correct=1),
            dict(id=1, title='How to fly to the moon?', text='Smoke weed 3', answers='100',
                 tags=['t1', 't2', 't3'],
                 author='Rubinov', rating=3, is_correct=0),
            dict(id=1, title='How to fly to the moon?', text='Choose blue tablet 3', answers='100',
                 tags=['t1', 't2', 't3'],
                 author='Morozov', rating=12, is_correct=1)

    ]

    current_page = _paginate(object_list, request)

    return render(request, 'questions/question.html', {
        'question': question,
        'comments': current_page.page(page_number)

    })



def tag(request, page_number=1):

    object_list = [
            dict(id=1, title='How to fly to the moon?', desc='Rly how?', answers='100',
                 tags=['c++', 'python', 'c#'], author='Ermakov',rating=123),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
                 tags=['c#', 'python'], author='Rubinov', rating=100),
            dict(id=1, title='How to fly to the moon?', desc='Rly how?', answers='100',
                tags=['c++', 'python', 'c#'], author='Ermakov', rating=123),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
                tags=['c#', 'python'], author='Rubinov', rating=100),
            dict(id=1, title='How to fly to the moon?', desc='Rly how?', answers='100',
             tags=['c++', 'python', 'c#'], author='Ermakov', rating=123),
            dict(id=1, title='hash code slayer', desc='why so easy?', answers='999',
             tags=['c#', 'python'], author='Rubinov', rating=100)
        ]

    current_page = _paginate(object_list, request)

    return render(request, 'questions/tag.html', {
        'questions': current_page.page(page_number)

    })


def hot(request, page_number=1):

    object_list = [
        dict(id=1, title='How to fly to the moon?', desc='Rly how?', answers='100',
             tags=['c++', 'python', 'c#'],
             author='Ermakov', rating=12),
        dict(id=1, title='hash code slayer hot 1', desc='why so easy? 1', answers='999',
             tags=['c++'], author='Rubinov', rating=100),
        dict(id=1, title='hash code slayer hot 2', desc='why so easy? 2', answers='999',
             tags=['python'], author='Rubinov', rating=100),
        dict(id=1, title='hash code slayer hot 3', desc='why so easy? 3', answers='999',
             tags=['c#'], author='Rubinov', rating=100),
        dict(id=1, title='hash code slayer hot 4', desc='why so easy? 4', answers='999',
             tags=['perl'], author='Rubinov', rating=100),
        dict(id=1, title='hash code slayer hot 5', desc='why so easy? 5', answers='999',
             tags=['perl'], author='Rubinov', rating=100),

    ]

    current_page = _paginate(object_list, request)

    return render(request, 'questions/hot.html', {
        'questions': current_page.page(page_number)
    })


def ask(request):
    return render(request, 'questions/ask.html', {'title': 'New question'})

