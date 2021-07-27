from django.shortcuts import render
from django.views.generic import View
import datetime
from shop import models


class TimeStat(View):

    def get(self, request):
        return render(request, 'report.html')

    def post(self, request):

        date_from = datetime.datetime.strptime(request.POST.get('date_from'), "%Y-%m-%dT%H:%M")
        date_to = datetime.datetime.strptime(request.POST.get('date_to'), "%Y-%m-%dT%H:%M")

        search_query = models.Order.objects.filter(created_date__range=[date_from, date_to])
        return render(request, 'report.html', {'search_query': search_query})

