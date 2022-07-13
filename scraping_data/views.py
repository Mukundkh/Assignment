from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.views import View
import requests

class ScrapingUrls(View):

    url = ""

    def get(self, request):
        #Fetch the HTML Data from the source website
        req_obj = requests.get(self.url)
        html_content = req_obj.content

        #Parse the HTML Content
        soup = BeautifulSoup(html_content, 'html.parser')

        #Filter from HTML DOM  by the respective class name and element
        list_elements = soup.find_all("li", class_="latest-stories__item")

        #Initializing the resultset to store the title and links of latest Stories
        result_set = []

        #Filtering DOM elements according to the usage
        for s in list_elements:
            title = s.find("h3").get_text()
            link = s.find("a").get('href')
            headline_object = {}
            headline_object['link'] = self.url + link
            headline_object['title'] = title
            result_set.append(headline_object)

        return JsonResponse(result_set, safe=False)
