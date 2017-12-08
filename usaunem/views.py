from django.shortcuts import render
from usaunem.Api.graph_to_plot import graphify
import json
def index(request):
    graph = graphify()
    list_of_dates = graph.getdates()
    list_of_threeAvg = graph.getthreemonthavg()
    list_of_twelveAvg = graph.gettwelvemonthavg()
    list_of_thirtySixAvg = graph.getthirtysixmonthavg()
    #return render(request, 'usaunem/home.html')


    chart = []

    for index, date in enumerate(list_of_dates):
        chart.append([
            date,
            float(list_of_threeAvg[index]),
            float(list_of_twelveAvg[index]),
            float(list_of_thirtySixAvg[index])
        ])

    return render(request, 'usaunem/home.html', {'list_of_dates':list_of_dates,
                                                 'list_of_threeAvg':list_of_threeAvg,
                                                 'list_of_twelveAvg':list_of_twelveAvg,
                                                'list_of_thirtySixAvg': list_of_thirtySixAvg,
                                                 'chart': json.dumps(chart)})
