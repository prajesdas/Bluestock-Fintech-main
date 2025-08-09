from django.db import models
from .utils import save_image_from_url

class IpoInfo(models.Model):
    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Coming', 'Coming'),
        ('New Listed', 'New Listed'),
    ]
    
    location = models.CharField(default="", max_length=255)
    company_logo_path = models.TextField()
    company_name = models.CharField(max_length=255)
    price_band = models.CharField(max_length=255)
    open = models.CharField(max_length=255)
    close = models.CharField(max_length=255)
    issue_size = models.CharField(max_length=255)
    issue_type = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    ipo_price = models.CharField(max_length=255)
    listing_price = models.CharField(max_length=255)
    listing_gain = models.CharField(max_length=255)
    listing_date = models.CharField(max_length=255)
    cmp = models.CharField(max_length=255)
    current_return = models.CharField(max_length=255)
    rhp = models.CharField(max_length=255)
    drhp = models.CharField(max_length=255)
    gain = models.BooleanField(default=False)
    exchange = models.CharField(default='NSE', max_length=50)
    company_logo = models.ImageField(upload_to='company_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        # Check if company_logo_path is provided and company_logo is not set
        if self.company_logo_path and not self.company_logo:
           save_image_from_url(self.company_logo_path, self, 'company_logo')
        super().save(*args, **kwargs)
