from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.views.generic.base import RedirectView, TemplateView, View
from django.views.generic import TemplateView
from log.function import change_date_to_english
import pymongo
from datetime import datetime
from django.http import Http404, HttpResponse

import io,csv


# Create your views here.


class Home(TemplateView):
    template_name = 'log/home.html'



class LogView(TemplateView):
    template_name = 'log/create_log.html'

    def post(self, request):
        as_date= self.request.POST.get('as_date')
        as_date1 = change_date_to_english(as_date, 2)

        ta_date=self.request.POST.get('ta_date')
        ta_date1 = change_date_to_english(ta_date, 2)

        myclient=pymongo.MongoClient('mongodb://localhost:27017/')
        mydb=myclient["my_database"]
        mycollection = mydb["logs"]
        print(mydb.list_collection_names())
        # mydict = {"username": "John2","timestamp":datetime.now()}
        # x=mycol.insert_one(mydict)
        result=mycollection.find({"timestamp":{'$gte':as_date1,'$lte':ta_date1}})
        print("result",result)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)
        writer.writerow(['id','signup','username'])


        for i in result:
            # print(result[i])
            id=i.get('_id')
            timestamp=i.get("timestamp")
            username=i.get("username")
            writer.writerow([id,timestamp,username])

        return response

