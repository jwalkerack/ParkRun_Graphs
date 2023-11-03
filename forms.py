from django import forms
from run.models import location, event
from django.core.validators import MinLengthValidator, MaxLengthValidator




def generateYears():
    Years = [""]
    YearsTuple = []
    e = event.objects.values('Date').distinct()
    eventList = list(e)
    for ee in eventList:
        eeYear = ee['Date'].year
        Years.append(eeYear)
    for item in Years:
        if item != "":
            x = [int(item),int(item)]
        else:
            x = [item,item]
        if x not in YearsTuple:
            YearsTuple.append(x)
    YearsTuple = tuple(YearsTuple)
    return YearsTuple

def generateLocations():
    Years = [""]
    YearsTuple = []
    e = location.objects.values('id','Date').distinct()
    eventList = list(e)
    for ee in eventList:
        eeYear = ee['Date'].year
        Years.append(eeYear)
    for item in Years:
        if item != "":
            x = [int(item),int(item)]
        else:
            x = [item,item]
        if x not in YearsTuple:
            YearsTuple.append(x)
    YearsTuple = tuple(YearsTuple)
    return YearsTuple

def generate_tuples(data):
    data = [(i ,i)for i in data]
    data = tuple(data)
    return data

def Int_Choice_Tups(A,B):
    C = []
    for o in range(A,B):
        C.append(o)
    data = [(i ,i)for i in C]
    data = tuple(data)
    return data

YEARS_CHOICES = generateYears()

GENDER_CHOICES = (("Male","Male"),("Female","Female"),("Both","Both"))



MONTH_CHOICES = ((1,'Jan'),(2,'Feb'),(3,'Mar'),
                    (4,"Apr"),(5,'May'),(6,'Jun'),(7,'July'),
                    (8,"Aug"),(9,'Sept'),(10,'Oct'),(11,'Nov'),(11,'Dec'))


GROUP_CHOICES = (('JM10', 'JM10'),
                 ('JW10', 'JW10'),
                 ('JM11-14', 'JM11-14'),
                 ('JW11-14', 'JW11-14'),
                 ('JM15-17', 'JM15-17'),
                 ('JW15-17', 'JW15-17'),
                 ('SM18-19', 'SM18-19'),
                 ('SW18-19', 'SW18-19'),
                 ('SM20-24', 'SM20-24'),
                 ('SW20-24', 'SW20-24'),
                 ('SM25-29', 'SM25-29'),
                 ('SW25-29', 'SW25-29'),
                 ('SM30-34', 'SM30-34'),
                 ('SW30-34', 'SW30-34'),
                 ('VM35-39', 'VM35-39'),
                 ('VW35-39', 'VW35-39'),
                 ('VM40-44', 'VM40-44'),
                 ('VW40-44', 'VW40-44'),
                 ('VM45-49', 'VM45-49'),
                 ('VW45-49', 'VW45-49'),
                 ('VM50-54', 'VM50-54'),
                 ('VW50-54', 'VW50-54'),
                 ('VM55-59', 'VM55-59'),
                 ('VW55-59', 'VW55-59'),
                 ('VM60-64', 'VM60-64'),
                 ('VW60-64', 'VW60-64'),
                 ('VM65-69', 'VM65-69'),
                 ('VW65-69', 'VW65-69'),
                 ('VM70-74', 'VM70-74'),
                 ('VW70-74', 'VW70-74'),
                 ('VM75-79', 'VM75-79'),
                 ('VW75-79', 'VW75-79'),
                 ('VM80-84', 'VM80-84'),
                 ('VW80-84', 'VW80-84'),
                 ('VM85-89', 'VM85-89'),
                 ('VW85-89', 'VW85-89'))




class RaceFilterForm(forms.Form):
    location = forms.ModelChoiceField(queryset=location.objects.all(),label='Location')

    event = forms.ModelChoiceField(queryset=event.objects.all(),label='Event')

    year = forms.ChoiceField(required=False, label='Occurred on Year',choices = YEARS_CHOICES)
    month = forms.ChoiceField(required=False, label='Occurred on Month',choices = MONTH_CHOICES)

class LocationForm(forms.Form):
    location = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'location-select'}),
        queryset=location.objects.all()
    )
    start = forms.ChoiceField(required=False, label='Start Year',choices = YEARS_CHOICES)
    end = forms.ChoiceField(required=False, label='Start Year',choices = YEARS_CHOICES)

class Time_Hist(forms.Form):
    location = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'location-select'}),
        queryset=location.objects.all()
    )
    start = forms.ChoiceField(required=False, label='From_Year',choices = YEARS_CHOICES)
    end = forms.ChoiceField(required=False, label='To_Year',choices = YEARS_CHOICES)
    gender = forms.ChoiceField(required=False, label='Gender',choices = GENDER_CHOICES)
    group = forms.ChoiceField(required=False, label='Group',choices = GROUP_CHOICES)

    base_hours = forms.ChoiceField(required=False, label='hours',choices = Int_Choice_Tups(0,3))
    base_minutes = forms.ChoiceField(required=False, label='minutes',choices = Int_Choice_Tups(0,60))
    base_seconds = forms.ChoiceField(required=False, label='seconds',choices = Int_Choice_Tups(0,60))

    bins = forms.ChoiceField(required=False, label='bins',choices = Int_Choice_Tups(1,60))

    low_hours = forms.ChoiceField(required=False, label='low_hours',choices = Int_Choice_Tups(0,3))
    low_minutes = forms.ChoiceField(required=False, label='low_minutes',choices = Int_Choice_Tups(0,60))
    low_seconds = forms.ChoiceField(required=False, label='low_seconds',choices = Int_Choice_Tups(0,60))

    high_hours = forms.ChoiceField(required=False, label='high_hours',choices = Int_Choice_Tups(0,3))
    high_minutes = forms.ChoiceField(required=False, label='high_minutes',choices = Int_Choice_Tups(0,60))
    high_seconds = forms.ChoiceField(required=False, label='high_seconds',choices = Int_Choice_Tups(0,60))
