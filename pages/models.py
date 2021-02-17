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
    tab = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class ServicepageImage(models.Model):
    content = models.ForeignKey(ServicepageContent, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='service/',
                              max_length=150, default='None/no-img.jpg')


class AboutpageContent(models.Model):
    name = models.CharField(max_length=150)
    roles = models.CharField(max_length=150, default='Contributors')
    quotes = models.TextField()

    def __str__(self):
        return self.name

class AboutpageImage(models.Model):
    content = models.ForeignKey(AboutpageContent, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='about/',
                              max_length=150, default='None/no-img.jpg')

class JoinpageContent(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title

class JoinpageImage(models.Model):
    content = models.ForeignKey(JoinpageContent, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='join/',
                              max_length=150, default='None/no-img.jpg')
