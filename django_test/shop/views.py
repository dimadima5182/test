from django.shortcuts import render
from django.views.generic import View
import datetime
from django.db import connection
from .utils import query_debugger

from django.db.models import Count
from shop import models


class TimeStat(View):
    @query_debugger
    def get(self, request):
        return render(request, 'report.html')

    @query_debugger
    def post(self, request):
        date_from = datetime.datetime.strptime(request.POST.get('date_from'), "%Y-%m-%dT%H:%M")
        date_to = datetime.datetime.strptime(request.POST.get('date_to'), "%Y-%m-%dT%H:%M")
        search_query = models.Order.objects.all()
        qs = search_query.filter(created_date__range=(date_from, date_to))

        return render(request, 'report.html', {'search_query': qs})


class Favorite(View):
    @query_debugger
    def get(self, request):
        empty_dict = {}
        data = models.OrderItem.objects.all().values('product_name').annotate(count=Count('product_name')).order_by('-count')[:20]
        return render(request, 'favorite.html', {'data': data})
