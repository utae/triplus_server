from django.contrib import admin
from trip_info.models import TripInfo, TripInfoDetail, TripInfoComment

admin.site.register(TripInfo)
admin.site.register(TripInfoDetail)
admin.site.register(TripInfoComment)
