from django.db import models
from django.core.validators import MinLengthValidator

class runner(models.Model):
    Name = models.CharField(
            max_length=100,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    ParkRunId = models.PositiveIntegerField()
    Gender = models.TextField()
    def __str__(self):
        return self.Name

class location(models.Model):
    Name = models.CharField(
            max_length=100,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")])
    def __str__(self):
        return self.Name

class event(models.Model):
    location =  models.ForeignKey(location, on_delete=models.CASCADE)
    number = models.CharField(max_length=200,default='#')

    Date =  models.DateTimeField()

    def __str__(self):
        return self.number

class timings(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    runner = models.ForeignKey(runner, on_delete=models.CASCADE)
    runnerPosition = models.TextField()
    runnerTime = models.CharField(max_length=100)
    runnerTimeInSeconds = models.PositiveIntegerField()
    runnerClub = models.CharField(max_length=100)
    runnerGroup = models.CharField(max_length=100)

    def __str__(self):
        return self.event.location.Name


class run_notes(models.Model):
    section = models.CharField(max_length=14)
    notes = models.CharField(
            max_length=100,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")])
    def __str__(self):
        return self.section