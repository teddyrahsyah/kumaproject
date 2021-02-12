from django.db import models

# Create your models here.
class HomepageContent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class HomepageImage(models.Model):
    content = models.ForeignKey(HomepageContent, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='home/', max_length=150, default='None/no-img.jpg')


class ServicepageContent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ServicepageImage(models.Model):
    content = models.ForeignKey(ServicepageContent, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='service/img/', max_length=150, default='None/no-img.jpg')
    icon = models.ImageField(upload_to='service/icon/', max_length=150, default='None/no-img.jpg')
