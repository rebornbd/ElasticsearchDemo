from django.urls import path

from .views import index as homePage, PublisherDocumentView

urlpatterns = [
    path('', homePage, name='homePage'),

    path('search', PublisherDocumentView.as_view({'get': 'list'})),
]
