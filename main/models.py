from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
class Post(models.Model):
    title= models.CharField(max_length=100, blank=True)
    content= models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    body = models.TextField()
    image = models.ImageField(blank= True,upload_to='other_pics')
    date_posted = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['date_posted']

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        img.save(self.image.path)

    def __str__(self):
        return 'Comment {}'.format(self.body)