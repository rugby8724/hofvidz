from django.db import models


from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Hall(models.Model):
    title = models.CharField(max_length=257)
    user = models.ForeignKey(User, related_name='halls', on_delete=models.CASCADE)

class Video(models.Model):
    title = models.CharField(max_length=257)
    url = models.URLField()
    youtube_id = models.CharField(max_length=257)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
