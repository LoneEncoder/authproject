from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from company.models import Company
from company.serializers import (CompanySerializer, CompanyDetailSerializer, SearchCompanySerializer,
                                 CreateCompanySerializer)
from company.pagination import StandardResultsSetPagination


class SearchCompanyView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SearchCompanySerializer
    queryset = Company.objects.order_by('name')
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'owner')


class ListCompanyView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanySerializer
    queryset = Company.objects.order_by('-created')
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('name', 'owner', 'members', 'project_from_scratch', 'earns_upwork')


class CreateCompanyView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateCompanySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class UpdateCompanyView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()


class DeleteCompanyView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()


class CompanyDetailView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()
