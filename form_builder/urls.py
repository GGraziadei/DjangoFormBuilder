from django.urls import path
from . import views

urlpatterns = [
    path('form/<int:form_id>/', views.create_form, name='create_form'),
]