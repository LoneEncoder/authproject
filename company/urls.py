from django.urls import path

from company.views import (SearchCompanyView, ListCompanyView, CreateCompanyView, DeleteCompanyView,
                           CompanyDetailView, UpdateCompanyView)

urlpatterns = [
    path('search/', SearchCompanyView.as_view()),
    path('list/', ListCompanyView.as_view()),
    path('create/', CreateCompanyView.as_view()),
    path('update/<pk>/', UpdateCompanyView.as_view()),
    path('delete/<pk>/', DeleteCompanyView.as_view()),
    path('<pk>/', CompanyDetailView.as_view()),
]
