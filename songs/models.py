from PIL import Image
from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse


class ViewCount(models.Model):
    ip = models.CharField(max_length=50, default=None)


class Upload(models.Model):
    CATE = (
        ('Videos', 'Videos'),
        ('Music', 'Music'),
        ('Crypto', 'Crypto'),
    )
    title = models.CharField(max_length=100)
    image = models.ImageField()
    file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mp3'])])
    content = models.TextField()
    category = models.CharField(max_length=1000, choices=CATE)
    date = models.DateTimeField(auto_now_add=True)
    views = models.ManyToManyField(ViewCount, related_name="views")

    class Meta:
        ordering = ['-date']

    def total_views(self):
        return self.views.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)


class Comment(models.Model):
        post = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name='comments')
        user = models.CharField(max_length=30)
        email = models.EmailField()
        body = models.TextField()
        date = models.DateTimeField(auto_now_add=True)
