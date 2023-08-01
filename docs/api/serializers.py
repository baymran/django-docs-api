import re
from rest_framework import serializers
from .models import Document, Organization, DocumentType

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('name',)


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ('name',)


class DocumentSerializer(serializers.ModelSerializer):
    organization = serializers.CharField()
    type = serializers.CharField()
    department_code = serializers.CharField()

    class Meta:
        model = Document
        fields = '__all__'

    def validate_organization(self, value):
        if not value:
            raise serializers.ValidationError("Field 'organization' is required.")

        try:
            organization = Organization.objects.get(name=value)
            return organization
        except Organization.DoesNotExist:
            raise serializers.ValidationError("Invalid organization name.")

    def validate_type(self, value):
        if not value:
            raise serializers.ValidationError("Field 'type' is required.")

        try:
            document_type = DocumentType.objects.get(name=value)
            return document_type
        except DocumentType.DoesNotExist:
            raise serializers.ValidationError("Invalid document type.")

    def validate_department_code(self, value):
        if not value:
            raise serializers.ValidationError("Field 'department_code' is required.")

        if not re.match(r'^\d{3}-\d{3}$', value):
            raise serializers.ValidationError("Invalid department code format. The format should be '999-999'.")

        return value

    def create(self, validated_data):
        organization = validated_data.pop('organization')
        document_type = validated_data.pop('type')

        return Document.objects.create(organization=organization, type=document_type, **validated_data)
