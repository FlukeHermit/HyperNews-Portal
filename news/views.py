from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class NewsView(View):
    def get(self, response, *args, **kwargs):
        html = '''
        <title> HyperNews Portal </title>
        <h1>Coming soon</h1>
        '''
        return HttpResponse(html)
# Create your views here.
