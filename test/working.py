def race_selector(request):
    ## The aim of function is Select a race.. The key elements are going

    import plotly.express as px
    if request.method == 'POST':
        form = RaceFilterForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            event_id = form.cleaned_data['event']

            return render(request, 'run/data.html', {'payload':html})
    else:
        form = RaceFilterForm()
    return render(request, 'run/dataview.html', {'form': form, 'payload':[]})



def event_visual(request,location_id, event_id):
    import plotly.express as px
    e = event.objects.filter(id=event_id)
    results = timings.objects.filter(event__in=e)
    ## You know have the query set that shows that results ...

    pstring = results.values_list('runnerPosition',flat=True)
    time = results.values_list('runnerTimeInSeconds',flat=True)
    pNumber = list(map(int, pstring))
    runners = [timing.runner for timing in results]
    gender = [runner.Gender for runner in runners]
    fig = px.scatter(x=pNumber, y=time, color=gender, title='The Race Scatter')
    fig.update_layout(
        shapes=[
            dict(
                type='line',
                x0=0,
                y0=1200,
                x1=max(pNumber),
                y1=1200,
                line=dict(
                    color="grey",
                    width=1,
                    dash='dash'
                )
            ),
            dict(
                type='line',
                x0=0,
                y0=1800,
                x1=max(pNumber),
                y1=1800,
                line=dict(
                    color="grey",
                    width=1,
                    dash='dash'
                )
            )
        ],
    annotations=[
            dict(
                x=max(pNumber),
                y=1200-50,
                text='Sub 20',
                xanchor='right',
                yanchor='middle',
                showarrow=False
            ),
            dict(
                x=max(pNumber),
                y=1800-50,
                text='Sub 30',
                xanchor='right',
                yanchor='middle',
                showarrow=False
            )
        ]
    )


    html = fig.to_html()

    return render(request, 'run/event_visual.html', {'data' : {'location_id' : location_id,'event_id':event_id , 'graph': html}})

from django.http import JsonResponse
from django.shortcuts import render
from run.models import event

def get_events(request):
    location_id = request.GET.get('location_id')
    events = event.objects.filter(location=location_id).values('id', 'name')
    return JsonResponse({'events': list(events)})