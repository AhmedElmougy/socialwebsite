from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
import misaka
# Create your models here.


class Group(models.Model):

    name   = models.CharField(max_length=250,unique=True)
    member = models.ManyToManyField(User, through='Membership')
    auther = models.ForeignKey(User, related_name='auther',on_delete=models.CASCADE,default='')
    image  = models.ImageField(upload_to='groups', blank=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,blank=True,default='')    
    created_at = models.DateField(auto_now_add=True)    
    slug   = models.SlugField(max_length=250,unique=True,allow_unicode=True)

    def save(self,*args, **kwargs):
        self.slug   = slugify(self.name) 
        self.description_html = misaka.html(self.description)
        
        super().save(*args, **kwargs) 

    class Meta:
        ordering = ["name"]


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("groups:group_details", kwargs={"pk":self.pk,"slug": self.slug})


class Membership(models.Model):
    group = models.ForeignKey("Group", related_name='group_members', on_delete=models.CASCADE)
    user  = models.ForeignKey(User , related_name='user_groups'  , on_delete=models.CASCADE) 

    class Meta:
        unique_together = ("group", "user")


   