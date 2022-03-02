from django.urls import path
from .views import BookApiView

urlpatterns = [
    path('', BookApiView.as_view()),
]