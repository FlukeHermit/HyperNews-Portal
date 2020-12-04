from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

import datetime
import json
import random
import sys

test_json = {
    "created": "2020-02-22 16:40:00",
    "text": "A new star appeared in the sky.",
    "title": "The birth of the star",
    "link": 9234732
}
# Create your views here.


class HomeView(View):
    def get(self, response, *args, **kwargs):
        #         html = '''
        # <title>HyperNews Page</title>
        # <h1>Coming soon</h1>
        # '''
        #         return HttpResponse(html)
        return redirect("/news/")


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
            news_list = json.load(json_file)
            query = request.GET.get('q')
            if query:
                news_list = [
                    news for news in news_list if query in news['title']]
            return render(request, "news/hypernews.html", context={"news_list": news_list})


class CreateView(View):
    news_links = []

    @classmethod
    def random_link(cls):
        while True:
            link = random.randrange(1, sys.maxsize)
            if link not in cls.news_links:
                cls.news_links.append(link)
                return link

    def get(self, request, *args, **kwargs):
        return render(request, "news/create.html")

    def post(self, request, *args, **kwargs):
        news = {}
        news['title'] = request.POST.get('title')
        news['text'] = request.POST.get('text')
        news['created'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        news['link'] = self.random_link()
        with open(settings.NEWS_JSON_PATH, 'r+') as news_file:
            news_list = json.load(news_file)
            news_list.append(news)
            news_file.seek(0)
            json.dump(news_list, news_file)
        return redirect('/news/')
