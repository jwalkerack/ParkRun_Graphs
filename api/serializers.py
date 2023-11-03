from rest_framework.serializers import ModelSerializer, SerializerMethodField
from run.models import timings, event, location



class TimingsSerializer(ModelSerializer):
    locationName = SerializerMethodField()
    eventNumber = SerializerMethodField()
    eventDate = SerializerMethodField()


    class Meta:
        model = timings
        fields = ('id', 'event', 'runner', 'runnerPosition', 'runnerTime',
                  'runnerTimeInSeconds', 'runnerClub', 'runnerGroup', 'locationName','eventNumber', 'eventDate')

    def get_locationName(self, obj):
        return obj.event.location.Name

    def get_eventNumber(self, obj):
        return obj.event.number

    def get_eventDate(self, obj):
        return obj.event.Date
