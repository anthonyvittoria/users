from django.http import Http404
from django.shortcuts import redirect

class MyAuthorization:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if not request.path == '/':
                return redirect('index')

        response = self.get_response(request)
        return response