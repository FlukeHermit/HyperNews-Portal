from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

import json

test_json = {
    "created": "2020-02-22 16:40:00",
    "text": "A new star appeared in the sky.",
    "title": "The birth of the star",
    "link": 9234732
}
# Create your views here.


class HomeView(View):
    def get(self, response, *args, **kwargs):
        html = '''
<title>HyperNews Page</title>
<h1>Coming soon</h1>
'''
        return HttpResponse(html)


class NewsView(View):
    def get(self, request, link, *args, **kwargs):

        with open(settings.NEWS_JSON_PATH) as json_file:
            news_json = json.load(json_file)

        news_feed = {}
        for news in news_json:
            if news["link"] == int(link):
                news_feed = news

        if test_json["link"] == int(link):
            news_feed = test_json

        return render(request, 'news/index.html', context=news_feed)

class HypernewsView(View):
    def get(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH) as json_file:
            return render(request, "news/hypernews.html", context={"news_list": json.load(json_file)})