from django.shortcuts import render
from usaunem.Api.graph_to_plot import graphify
import json
def index(request):


    graph = graphify()
    last_date = graph.getLastDate()
    list_of_dates = graph.getdates()
    list_of_values = graph.getValues()
    list_of_threeAvg = graph.getthreemonthavg()
    list_of_twelveAvg = graph.gettwelvemonthavg()
    list_of_thirtySixAvg = graph.getthirtysixmonthavg()


    chart = []


    for index, date in enumerate(list_of_dates):
        chart.append([
            date,
            float(list_of_values[index]),
            float(list_of_threeAvg[index]),
            float(list_of_twelveAvg[index]),
            float(list_of_thirtySixAvg[index])
        ])

    context_dict = {}
    context_dict['chart'] = json.dumps(chart)
    context_dict['last_date'] = last_date

    return render(request, 'usaunem/home.html', context_dict)
