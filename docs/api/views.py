from rest_framework import generics
from .models import Document, Organization, DocumentType
from .serializers import DocumentSerializer, OrganizationSerializer, DocumentTypeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class OrganizationListView(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class DocumentTypeListView(generics.ListAPIView):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer


class DocumentCreateView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        type_name = self.request.data.get('type')
        org_name = self.request.data.get('organization')

        if not type_name:
            return Response({"type": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        if not org_name:
            return Response({"organization": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        try:
            document_type = DocumentType.objects.get(name=type_name)
        except DocumentType.DoesNotExist:
            return Response({"type": ["Invalid document type."]}, status=status.HTTP_400_BAD_REQUEST)

        try:
            organization = Organization.objects.get(name=org_name)
        except Organization.DoesNotExist:
            return Response({"organization": ["Invalid organization."]}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(type=document_type, organization=organization)


class DocumentUpdateView(generics.UpdateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_update(self, serializer):
        type_name = self.request.data.get('type')
        org_name = self.request.data.get('org')

        if not type_name:
            return Response({"type": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        if not org_name:
            return Response({"org": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        try:
            document_type = DocumentType.objects.get(name=type_name)
        except DocumentType.DoesNotExist:
            return Response({"type": ["Invalid document type."]}, status=status.HTTP_400_BAD_REQUEST)

        try:
            organization = Organization.objects.get(name=org_name)
        except Organization.DoesNotExist:
            return Response({"org": ["Invalid organization."]}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(type=document_type, organization=organization)


class DocumentDeleteView(generics.DestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(self.get_queryset(), pk=kwargs['pk'])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
