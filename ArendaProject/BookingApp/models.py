from django.db import models
from django.contrib.auth.models import User

# Модель жилплощади
class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)  # Поле для URL изображения (необязательное)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

# Модель бронирования
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_guests = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('cancelled', 'Cancelled')
        ],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f"Booking #{self.id} - {self.user.username}"