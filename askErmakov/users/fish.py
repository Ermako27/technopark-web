def current_user(request):
    return dict(
        current_user=dict(
            login='Maxim Ermakov',
            id=1,
            loged=0
        ),
    )