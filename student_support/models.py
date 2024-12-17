from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100)  # FontAwesome class

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question

class Counselor(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    additional_info = models.TextField()
    email = models.EmailField()
    image = models.ImageField(upload_to='counselors/')

    def __str__(self):
        return self.name