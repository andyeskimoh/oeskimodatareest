from django.conf.urls import url, include
from  django.views.generic import  ListView, DetailView
from points.models import  Points


urlpatterns = [

    url(r'^$', ListView.as_view(queryset=Points.objects.all(),
        template_name="points/points.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model= Points, template_name= "points/point.html"))
]