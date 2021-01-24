from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title      = models.CharField(max_length=250)
    body       = models.TextField()
    auther     = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    image        = models.ImageField(upload_to='post_pics', blank=True)
    group      = models.ForeignKey("groups.Group",related_name='posts', on_delete=models.CASCADE)
    

    class Meta:
        ordering=('created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:post_details", kwargs={"pk": self.pk})



class Comment(models.Model):
    post   = models.ForeignKey("posts.Post",related_name='comments' ,on_delete=models.CASCADE)
    auther = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text   = models.TextField() 
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse("post:post_details", kwargs={"pk": self.post.id})
