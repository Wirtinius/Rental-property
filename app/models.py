from django.db import models
import uuid

class PropertyPhoto(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_photos/')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['property', 'order']

    def __str__(self):
        return f"Photo for Property: {self.property.id}"


class MyUUIDModel(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Property(MyUUIDModel):

    PROPERTY_TYPES = (
        ('rent', 'Rental'),
        ('buy', 'Buy'),
        ('sale', 'Sale'),
    )

    BUY_PROPERTY_TYPES = (
        ('flat', 'Flat'),
        ('land', 'Land for sale'),
        ('office', 'Office for Sale')
    )

    property_name = models.CharField(max_length=30)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    location_pincode = models.CharField(max_length=10)
    location_city = models.CharField(max_length=50)
    location_area = models.CharField(max_length=50)
    landmark = models.CharField(max_length=100)
    owner_or_agent = models.BooleanField(default=True)  # True for owner, False for agent
    video = models.FileField(upload_to='property_videos/', blank=True, null=True)
    mobile_number = models.CharField(max_length=15)
    summary = models.TextField()

    # Fields for rental properties
    rent_per_month = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    available_from = models.DateField(blank=True, null=True)
    owner_name = models.CharField(max_length=100, blank=True, null=True)
    owner_id_document = models.FileField(upload_to='owner_documents/', blank=True, null=True)

    # Fields for buying/selling properties
    property_type_buy = models.CharField(max_length=20, choices=BUY_PROPERTY_TYPES, blank=True, null=True)
    property_documents = models.FileField(upload_to='property_documents/', blank=True, null=True)
    owner_info = models.TextField(blank=True, null=True)


class VisitRequest(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(default='pending', null=True, blank=True, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visit Request for Property: {self.property.property_name}"