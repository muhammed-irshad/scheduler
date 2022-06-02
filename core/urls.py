from django.urls import path
from .views import RegisterTime, AvailableTimeSlots

urlpatterns = [
    path("register_time/", RegisterTime.as_view()),
    path("available_slots/", AvailableTimeSlots.as_view()),
]