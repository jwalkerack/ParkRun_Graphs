from django.shortcuts import render

from django.shortcuts import get_object_or_404
from run.models import location, event, runner, timings
from django.shortcuts import redirect
# Create your views here.


from run.forms import RaceFilterForm , LocationForm , Time_Hist

def time_to_seconds(hours, minutes, seconds):
    return (hours * 3600) + (minutes * 60) + seconds



def make_Plots(A,B,C,D):
    bins = int(D)
    import matplotlib.pyplot as plt
    import numpy as np
    min_x = np.min(A['runnerTimeInSeconds'])
    max_x = np.max(A['runnerTimeInSeconds'])
    # create a figure with 3 rows and 1 column
    fig, ax = plt.subplots(3, 1,figsize=(5, 10))
    fig.subplots_adjust(hspace=0.4)
    # create the first histogram
    ax[0].hist(A['runnerTimeInSeconds'],density=False,histtype='bar',align='left',orientation='vertical',edgecolor = "black",bins=bins,color='aqua')
    ax[0].set_title("all data")
    ax[0].set_xlabel('Time (In Seconds)')
    ax[0].set_xlim([min_x, max_x])
    # create the second histogram
    ax[1].hist(B['runnerTimeInSeconds'],density=False,histtype='bar',align='left',orientation='vertical',edgecolor = "black",bins=bins,color='aqua')
    ax[1].set_title("runner__Gender")
    ax[1].set_xlabel('Time (In Seconds)')
    ax[1].set_xlim([min_x, max_x])
# create the third histogram
    ax[2].hist(C['runnerTimeInSeconds'],density=False,histtype='bar',align='left',orientation='vertical',edgecolor = "black",bins=bins,color='aqua')
    ax[2].set_title("runnerGroup")
    ax[2].set_xlabel('Time (In Seconds)')
    ax[2].set_xlim([min_x, max_x])
    return fig

def make_Plots2(Male,Female,D):
    bins = int(D)
    import matplotlib.pyplot as plt
    import numpy as np
    min_x = min(np.min(Male['runnerTimeInSeconds']),np.min(Female['runnerTimeInSeconds']))
    max_x = max(np.max(Male['runnerTimeInSeconds']), np.max(Female['runnerTimeInSeconds']))
    # create a figure with 3 rows and 1 column
    fig, ax = plt.subplots(2, 1,figsize=(10, 6))
    fig.subplots_adjust(hspace=0.5)
    # create the first histogram
    ax[0].hist(Male['runnerTimeInSeconds'],density=False,histtype='bar',align='left',orientation='vertical',edgecolor = "black",bins=bins,color='aqua')
    ax[0].set_title("Male")
    ax[0].set_xlabel('Time (In Seconds)')
    ax[0].set_xlim([min_x, max_x])
    # create the second histogram
    ax[1].hist(Female['runnerTimeInSeconds'],density=False,histtype='bar',align='left',orientation='vertical',edgecolor = "black",bins=bins,color='pink')
    ax[1].set_title("Female")
    ax[1].set_xlabel('Time (In Seconds)')
    ax[1].set_xlim([min_x, max_x])
# create the third histogram

    return fig





def make_Plots1(A,B,C,D):
    bins = int(D)
    import matplotlib.pyplot as plt
    import numpy as np
    min_x = np.min(A['runnerTimeInSeconds'])
    max_x = np.max(A['runnerTimeInSeconds'])
    # create a figure with 3 rows and 1 column
    fig, ax = plt.subplots(1, 1,figsize=(10, 6))
    fig.subplots_adjust(hspace=0.5)
    # create the first histogram
    ax[0].hist(A['runnerTimeInSeconds'],density=False,histtype='bar',align='left',orientation='vertical',edgecolor = "black",bins=bins,color='aqua')
    ax[0].set_title("all data")
    ax[0].set_xlabel('Time (In Seconds)')
    ax[0].set_xlim([min_x, max_x])
    # create the second histogram

# create the third histogram

    return fig


def time_visual(request):
    import pandas as pd
    import mpld3
    if request.method == 'POST':
        Time_Form = Time_Hist(request.POST)
        if Time_Form.is_valid():
            locations = Time_Form.cleaned_data['location']
            start_year = Time_Form.cleaned_data['start']
            end_year = Time_Form.cleaned_data['end']
            gender = Time_Form.cleaned_data['gender']
            group = Time_Form.cleaned_data['group']
            theBins = Time_Form.cleaned_data['bins']

            low_hour = Time_Form.cleaned_data['low_hours']
            low_minutes = Time_Form.cleaned_data['low_minutes']
            low_seconds = Time_Form.cleaned_data['low_seconds']
            high_hour = Time_Form.cleaned_data['high_hours']
            high_minutes = Time_Form.cleaned_data['high_minutes']
            high_seconds = Time_Form.cleaned_data['high_seconds']

            low_time = time_to_seconds(int(low_hour), int(low_minutes), int(low_seconds))
            high_time = time_to_seconds(int(high_hour), int(high_minutes), int(high_seconds))

            event_list = event.objects.filter(location__in=locations)
            if start_year:
                event_list = event_list.filter(Date__year__gte=start_year)
            if end_year:
                event_list = event_list.filter(Date__year__lte=end_year)
            timings_data = timings.objects.filter(event__in=event_list).values('event__location_id', 'event__location__Name', 'runnerTimeInSeconds','runner', 'runner__Gender', 'event__Date', 'runnerGroup')
            timings_data = timings_data.filter(runnerTimeInSeconds__gte=low_time)
            timings_data = timings_data.filter(runnerTimeInSeconds__lte=high_time)

            df_Base = pd.DataFrame.from_records(timings_data)

            lowest_time_df = df_Base.sort_values(by=['runner','event__location_id','runner__Gender','runnerTimeInSeconds']).drop_duplicates(subset=['runner','event__location_id','runner__Gender'], keep='first')
            sorted_lowest_time_df = lowest_time_df.sort_values(by=['runnerTimeInSeconds'])
            df_Male = sorted_lowest_time_df[sorted_lowest_time_df['runner__Gender'] == 'Male']
            df_Female = sorted_lowest_time_df[sorted_lowest_time_df['runner__Gender'] == 'Female']
            x = df_Base.shape[0]
            V = str(type(theBins))

            D = make_Plots2(df_Male,df_Female,theBins)

            html_plot = mpld3.fig_to_html(D)

            df_html = lowest_time_df.to_html()
            #return render(request, 'run/time_visual.html',{'dataframe': df_Base})
            return render(request, 'run/time_visual.html',{'form':Time_Form, 'data':html_plot , 'payload':df_html , 'dataframe': df_Base})
    else:
        Time_Form = Time_Hist()
    return render(request, 'run/time_visual.html',{'form':Time_Form , 'payload':'hmmm'})




def header(request):
    return render(request, 'run/index.html')

def participation(request):
    import pandas as pd
    if request.method == 'POST':
        Locaform = LocationForm(request.POST)
        if Locaform.is_valid():
            locations = Locaform.cleaned_data['location']
            start_year = Locaform.cleaned_data['start']
            end_year = Locaform.cleaned_data['end']
            event_list = event.objects.filter(location__in=locations).select_related('location')
            if start_year:
                event_list = event_list.filter(Date__year__gte=start_year)
            if end_year:
                event_list = event_list.filter(Date__year__lte=end_year)
            timings_data = timings.objects.filter(event__in=event_list).values('event__id', 'event__Date', 'event__location__id', 'event__location__Name', 'runner__id')
            df = pd.DataFrame.from_records(timings_data)
            df['date_column'] = df['event__Date'].dt.date



            #### Add in the Count of the Runneres

            newFrame = df.groupby(['event__location__Name','date_column']).size().reset_index(name='RunnerCount')

            places = ['Aberdeen parkrun', 'Aviemore parkrun',  'Camperdown parkrun, Dundee', 'Crathes Castle parkrun',  'Elgin parkrun',
                        'Ellon parkrun', 'Faskally Forest parkrun', 'Forfar Loch parkrun', 'Hazlehead parkrun, Aberdeen',
                        'Montrose parkrun', 'Perth parkrun', 'Stonehaven parkrun',  'Torvean parkrun', 'Ury Riverside parkrun', 'West Links parkrun']

            colors = ['rgb(255,0,0)','rgb(0,255,0)','rgb(0,0,255)','rgb(255,255,0)','rgb(255,0,255)',
            'rgb(0,255,255)','rgb(255,255,255)','rgb(0,0,0)','rgb(127,127,127)','rgb(127,0,0)','rgb(0,127,0)'
            ,'rgb(0,0,127)','rgb(127,127,0)','rgb(127,0,127)','rgb(0,127,127)']

            color_dict = dict(zip(places, colors))

            import math
            import plotly.graph_objects as go
            import plotly.subplots as sp
            traces = []
            df_filtered = newFrame

            pp = df_filtered['RunnerCount'].max()

            pp = math.ceil(pp / 100.0) * 100

            # Loop through the unique events
            for e, e_df in df_filtered.groupby(['event__location__Name']):

                # Create a trace for the current event
                trace = go.Scatter(
                    x=e_df['date_column'],
                    y=e_df['RunnerCount'],
                    mode='markers',
                    name=e,
                    marker=dict(
                        color=color_dict.get(e, 'gray')
                    )
                )
                # Append the trace to the list
                traces.append(trace)

            # Create a subplot with the traces
            fig = sp.make_subplots(rows=len(traces), cols=1, shared_xaxes=True, shared_yaxes=True)

            # Add the traces to the subplot
            for i, trace in enumerate(traces):
                fig.append_trace(trace, i+1, 1)

            # Update the layout of the subplot
            fig.update_layout(
                barmode='stack',
                height=800,
                xaxis=dict(
                    showgrid=True,
                    zeroline=False,
                    ticklen= 5, tickwidth= 2
                ),
                yaxis=dict(
                    showgrid=True,
                    zeroline=False,
                    range=[0, pp],
                )
            )
            # Update the y-axis properties of all subplots
            fig.update_yaxes(range=[0, pp + 70 ])
            fig.update_xaxes( zeroline=False, ticklen=5, tickwidth=2)



            # Show the plot
            fig.show()
            html = fig.to_html()

            geeks_object = newFrame.to_html()
            return render(request, 'run/participation.html',{'form2':Locaform, 'timings_data':html})
        else:
            message = "Form contains errors, please correct them before submitting."
            form_errors = Locaform.errors
            return render(request, 'run/participation.html',{'form2':Locaform , 'message':message ,'errors':from_errors})

    else:
        Locaform = LocationForm()
        message = ''
        from_errors = Locaform.errors
    return render(request, 'run/participation.html', {'form2':Locaform , 'message':message ,'errors':from_errors})

def about(request):
    return render(request, 'run/about.html')

def location_summary(request):
    locations = location.objects.all()
    location_data = []
    for l in locations:
        location_events = event.objects.filter(location=l)
        event_count = location_events.count()
        runner_count = runner.objects.filter(timings__event__in=location_events).distinct().count()
        total_runs = timings.objects.filter(event__in=location_events).count()
        location_data.append({
            'name': l.Name,
            'location_id': l.id,
            'event_count': event_count,
            'runner_count': runner_count,
            'total_runs': total_runs
        })
    return render(request, 'run/location_summary.html', {'location_data': location_data})

def event_summary(request, location_id):
    l = get_object_or_404(location, pk=location_id)
    events = event.objects.filter(location=l).order_by('-Date')
    event_data = []
    for e in events:
        event_timings = timings.objects.filter(event=e)
        runner_count = event_timings.count()
        event_data.append({
            'location_id': l.id,
            'event_id': e.id,
            'event_number': e.number,
            'runner_count': runner_count,
            'date': e.Date.strftime('%d/%m/%Y')
        })
    return render(request, 'run/event_summary.html', {'location': l, 'event_data': event_data})


def event_details(request, event_id, location_id):
    e = get_object_or_404(event, pk=event_id)
    l = get_object_or_404(location, pk=location_id)
    results = timings.objects.filter(event=e).order_by('runnerPosition')
    runner_data = []
    for r in results:
        runner_data.append({
            'position': int(r.runnerPosition),  # Convert runnerPosition to integer
            'name': r.runner.Name,
            'time': r.runnerTime,
            'club': r.runnerClub,
            'group': r.runnerGroup,
            'runner_id': r.runner.id,
        })
    # Sort runner_data by position
    runner_data = sorted(runner_data, key=lambda x: x['position'])
    return render(request, 'run/event_details.html', {'location': l, 'event': e, 'runner_data': runner_data})


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


def runner_details(request, runner_id):
    B = get_object_or_404(runner, pk=runner_id)
    runs = timings.objects.filter(runner=runner_id)
    Races = []
    for r in runs:
        Races.append({
            'Location': r.event.location.Name,
            'RunDate': r.event.Date,  # Include RunDate field in the dictionary
            'EventNum': r.event.number,
            'position': int(r.runnerPosition),  # Convert runnerPosition to integer
            'time': r.runnerTime,
            'club': r.runnerClub,
            'group': r.runnerGroup
        })
    # Sort Races by RunDate in reverse order (most recent first)
    Races = sorted(Races, key=lambda x: x['RunDate'], reverse=True)
    # Format RunDate fields as strings in the '%d/%m/%Y' format
    for race in Races:
        race['RunDate'] = race['RunDate'].strftime('%d/%m/%Y')
    return render(request, 'run/runner_details.html', {'runner_data': Races, 'yy': B})



def race_filter_view(request):
    if request.method == 'POST':
        Raceform = RaceFilterForm(request.POST)
        Locaform = LocationForm(request.POST)
        if Raceform.is_valid():
            l = Raceform.cleaned_data['location']
            e = Raceform.cleaned_data['event']
            return redirect('event_visual', location_id=l.id, event_id=e.id)
        else:
            message = "Form contains errors, please correct them before submitting."
            form_errors = Raceform.errors
        if Locaform.is_valid():
            l = Locaform.cleaned_data['location']
            st = Locaform.cleaned_data['start']
            ed = Locaform.cleaned_data['end']
            print(form2.data)
    else:
        Raceform = RaceFilterForm()
        Locaform = LocationForm()
        message = ""
        form_errors = None

    return render(request, 'run/dataview.html', {'form': Raceform, 'form2':Locaform, 'message': message, 'form_errors': form_errors, 'payload':[]})

from django.http import JsonResponse
from django.shortcuts import render
from run.models import event

from django.http import JsonResponse, HttpResponseBadRequest

def get_events(request):
    location_id = request.GET.get('location_id')
    year = request.GET.get('year')
    month = request.GET.get('month')
    try:
        location_id = int(location_id)
        events = event.objects.filter(location_id=location_id)
        if year:
            events = events.filter(Date__year=year)
        if month:
            events = events.filter(Date__month=month)
        events = events.values()
        return JsonResponse({'events': list(events)})
    except (ValueError, TypeError):
        return HttpResponseBadRequest()



