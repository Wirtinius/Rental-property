
from django.contrib import admin
from .models import Property, PropertyPhoto, VisitRequest

class PropertyPhotoInline(admin.TabularInline):
    model = PropertyPhoto
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_type', 'location_pincode', 'location_city')
    list_filter = ('property_type', 'location_city')
    search_fields = ('title', 'location')
    actions = ['approve_properties', 'reject_properties']
    inlines = [PropertyPhotoInline]  # Include the PropertyPhotoInline form

    def approve_properties(self, request, queryset):
        queryset.update(status='approved')

    def reject_properties(self, request, queryset):
        queryset.update(status='rejected')

    approve_properties.short_description = "Approve selected properties"
    reject_properties.short_description = "Reject selected properties"
    fieldsets = (
        ('Basic Information', {
            'fields': ('property_name', 'property_type', 'location_pincode', 'location_city', 'location_area', 'landmark', 'owner_or_agent', 'mobile_number', 'summary'),
        }),
        ('Rental Property Details', {
            'fields': ('rent_per_month', 'deposit', 'available_from', 'owner_name', 'owner_id_document'),
            'classes': ('rental',),  # This class will be used to hide/show this fieldset
        }),
        ('Buying/Selling Property Details', {
            'fields': ('property_type_buy', 'property_documents', 'owner_info'),
            'classes': ('buy-sell',),  # This class will be used to hide/show this fieldset
        }),
    )

    def get_fieldsets(self, request, obj=None):
        # Hide/show fieldsets based on the property_type value
        fieldsets = super().get_fieldsets(request, obj)
        if obj and obj.property_type == 'rental':
            fieldsets[1][1]['classes'] = ('rental',)
            fieldsets[2][1]['classes'] = ()
        elif obj and obj.property_type == 'buy':
            fieldsets[1][1]['classes'] = ()
            fieldsets[2][1]['classes'] = ('buy-sell',)
        else:
            fieldsets[1][1]['classes'] = ()
            fieldsets[2][1]['classes'] = ()

        return fieldsets


# admin.site.register(PropertyPhoto)
admin.site.register(Property, PropertyAdmin)
admin.site.register(VisitRequest)

