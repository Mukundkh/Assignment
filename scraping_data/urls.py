from django.urls import path

from scraping_data.views import ScrapingUrls

urlpatterns = [
    path('', ScrapingUrls.as_view(url="https://time.com")),
]
