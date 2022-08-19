
from django.urls import path, include

from myapp.views import DRFPaginationSampleView


app_urls = [
    path("paginationsample/", DRFPaginationSampleView.as_view()),
]
