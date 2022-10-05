from rest_framework import serializers
from company.models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'owner', 'members', 'project_from_scratch', 'earns_upwork', 'benefits', 'contact_us', 'updated',)


class SearchCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'owner', 'members', 'project_from_scratch', 'earns_upwork', 'benefits', 'contact_us',)


class CreateCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id', 'name', 'owner', 'members', 'project_from_scratch', 'earns_upwork', 'benefits', 'contact_us',]
        extra_kwargs = {
            "name": {"required": True},
            "owner": {"required": True},
            "members": {"required": True},
            "project_from_scratch": {"required": True},
            "earns_upwork": {"required": True},
            "benefits": {"required": True},
            "contact_us": {"required": True},
        }

    def create(self, validated_data):
        return Company.objects.create(**validated_data)


class CompanyDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'owner', 'members', 'project_from_scratch', 'earns_upwork', 'benefits', 'contact_us',)
