import json
from datetime import datetime

from run.models import runner, location, event , timings

def isThere(A,B):
    try:
        C = B[A]
    except:
        C = None
    return C

def convert_to_seconds(input_string: str) -> int:
    if input_string is None:
        return 0
    time_parts = input_string.split(':')
    time_parts = [int(part) for part in time_parts]
    if len(time_parts) == 3:
        return 3600 * time_parts[0] + 60 * time_parts[1] + time_parts[2]
    elif len(time_parts) == 2:
        return 60 * time_parts[0] + time_parts[1]
    elif len(time_parts) == 1:
        return time_parts[0]
    else:
        return 0



def convert_to_date(input_string: str) -> datetime:
    return datetime.strptime(input_string, '%d/%m/%Y')

def geteventrow(data):
    row = [isThere('eventName',data),isThere('eventDate',data),isThere('eventNumber',data)]
    row[1] = convert_to_date(row[1])
    results = isThere('results',data)
    return [row,results]



def run():
    the_file = r'run/data/openAI_Chatbot.json'
    with open(the_file, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        for item in data:
            eventprocess = geteventrow(item)
            eventrow = eventprocess[0]
            l, created = location.objects.get_or_create(Name=eventrow[0])
            e, created = event.objects.get_or_create(number=eventrow[2],Date =eventrow[1] ,location = l)

            results = eventprocess[1]
            for runner1 in results:



                club = runner1[0]
                name = runner1[1]
                raceposition = runner1[2]
                genderGroup = runner1[3]
                gender = runner1[4]
                runnerId = runner1[5]
                stringTime = runner1[6]
                timeInSecs = convert_to_seconds(stringTime)
                if runnerId is None:
                    pass
                else:

                    r, created = runner.objects.get_or_create(Name=name,ParkRunId =runnerId,Gender=gender)
                    t , crearted = timings.objects.get_or_create(event=e,runner= r
                    ,runnerPosition = raceposition,runnerTime= stringTime , runnerClub =club,runnerGroup=genderGroup,runnerTimeInSeconds=timeInSecs )
