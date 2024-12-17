from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='club_logos/')
    established_year = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Moderator(models.Model):
    club = models.ForeignKey(Club, related_name='moderators', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='moderator_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    club = models.ForeignKey(Club, related_name='members', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='member_images/', blank=True, null=True)

    def __str__(self):
        return self.name

    
class Slider(models.Model):
    club = models.ForeignKey(Club, related_name='sliders', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='sliders/')
    order = models.PositiveIntegerField(default=0, help_text="Order of the slide in the slider.")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title if self.title else "Slider Item"