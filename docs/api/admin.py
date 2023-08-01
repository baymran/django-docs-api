from django.contrib import admin
from .models import Document, Organization, DocumentType


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'organization', 'series', 'number', 'date_of_issue', 'department_code', 'main',
                    'archival']
    list_filter = ['type', 'organization', 'main', 'archival']
    search_fields = ['type', 'organization']
    date_hierarchy = 'date_of_issue'
    actions = ['make_main', 'make_archival']

    def make_main(self, request, queryset):
        queryset.update(main=True)

    def make_archival(self, request, queryset):
        queryset.update(archival=True)

    make_main.short_description = "Make selected documents main"
    make_archival.short_description = "Make selected documents archival"


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Document, DocumentAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
