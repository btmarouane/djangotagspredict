from django.urls import path
from . import views

urlpatterns = [
    path('api/predict', views.predict),
    path('api/result', views.result),

]