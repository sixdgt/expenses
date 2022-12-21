from django.urls import path
from .views import PreferenceView

urlpatterns = [
    path('', PreferenceView.as_view(), name="preferences"),
]