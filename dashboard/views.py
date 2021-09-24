from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

from .models import Cases

cursor = connection.cursor()
def cases(request):
    
    cursor.execute("select Date(Date) as Date, sum(count) as Total, sum(CASE WHEN District='North Goa' THEN count ELSE 0 END) as NorthGoa, sum(CASE WHEN District='South Goa' THEN count ELSE 0 END) as SouthGoa, sum(CASE WHEN District='Unknown' THEN count ELSE 0 END) as Unknown from goa_covid_sheet group by date order by date desc")

    cdata = dictfetchall(cursor)
    print(cdata)
    
    cursor.execute("select town as Locations, count as Cases from goa_covid_sheet where Date = '2020-07-17' order by count desc limit 10")

    ddata = dictfetchall(cursor)
    print(ddata)
    
    cursor.execute("select max(Date) as Date from goa_covid_sheet")
    hdate = dictfetchall(cursor)
    print(hdate)
    
    cursor.execute("select sum(CASE WHEN District='North Goa' THEN count ELSE 0 END) as NorthGoa, sum(CASE WHEN District='South Goa' THEN count ELSE 0 END) as SouthGoa, sum(CASE WHEN District='Unknown' THEN count ELSE 0 END) as Unknown from goa_covid_sheet")
    total = dictfetchall(cursor)
    print(hdate)
    
    return render(request, 'dashboard/home.html', {'CASEDATA':cdata, 'DATEDATA':ddata, 'Total':total})




def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) 
            for row in cursor.fetchall()
           ]
           
