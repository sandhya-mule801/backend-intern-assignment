from django.urls import path
from .views import notes, note_detail

urlpatterns = [
    path('', notes),
    path('<int:id>/', note_detail),
]
