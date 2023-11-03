from django.utils import timezone
import random
from run.models import run_notes

def run():

    run_notes.objects.all().delete()
    section_choices = ["Weather", "Course", "Crowd", "Facilities", "Organization"]
    notes_choices = ["Good", "Average", "Poor", "Very Good", "Very Poor"]

    for i in range(10):
        s = random.choice(section_choices)
        n = random.choice(notes_choices)
        x, created = run_notes.objects.get_or_create(section=s,notes=n)
