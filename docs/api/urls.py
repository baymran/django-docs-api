from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentListCreateView, DocumentRetrieveUpdateView, OrganizationListView, DocumentTypeListView,\
    DocumentDeleteView

urlpatterns = [
    path('documents/', DocumentListCreateView.as_view(), name='Documents List'),
    path('documents/<int:pk>/', DocumentRetrieveUpdateView.as_view(), {'put': 'update', 'patch': 'partial_update'}, name='Document Update'),
    path('organizations/', OrganizationListView.as_view(), name='organization-list'),
    path('document-types/', DocumentTypeListView.as_view(), name='document-type-list'),
    path('documents/<int:pk>/delete/', DocumentDeleteView.as_view(), {'delete': 'destroy'}, name='document-delete'),
]
