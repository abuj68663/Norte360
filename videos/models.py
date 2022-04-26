from PIL import Image
from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse


class Videos(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mp3'])])
    content= models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video-detail', kwargs={'pk': self.pk})

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)

