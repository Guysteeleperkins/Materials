from django.db import models
from django.utils.text import slugify
from datetime import date
from cloudinary.models import CloudinaryField

class Event(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('upcoming', 'Upcoming'),
        ('past', 'Past'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    ticket_link = models.URLField(blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    event_date = models.DateField(blank=True, null=True)  # Optional event date

    def save(self, *args, **kwargs):
        # Automatically set the slug if it's not set
        if not self.slug:
            self.slug = slugify(self.title)

        # Automatically set the status based on the event date, if provided
        if self.event_date:
            today = date.today()
            if self.event_date < today:
                self.status = 'past'
            elif self.event_date >= today and self.status != 'draft':
                self.status = 'upcoming'

        super().save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.title
