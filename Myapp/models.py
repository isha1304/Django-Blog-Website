from django.db import models
from django.db.models import Model
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor.fields import RichTextField

# Create your models here.
# class Category(models.Model):
#     name=models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.name
    
#     def get_absolute_url(self):
#         #return reverse('article-detail', args=(str(self.id)))
#         return reverse('blog-home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=4000,default="Write your bio here")
    profile_pic =  models.ImageField(null=True, blank= True,upload_to="images/profile/")
    # website_url = models.CharField(max_length=255,null=True, blank= True)
    facebook_url = models.CharField(max_length=255,null=True, blank= True)
    twitter_url = models.CharField(max_length=255,null=True, blank= True)
    Instagram_url = models.CharField(max_length=255,null=True, blank= True)
    # linkedin_url = models.CharField(max_length=255,null=True, blank= True)

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('blog-home')
        
class Post(models.Model):
    # id=models.AutoField(primary_key=True)
    # header_image = models.ImageField(null=True, blank= True,upload_to="post_images/")
    title=models.CharField(max_length=1000)
    title_tag=models.CharField(max_length=255,default='home')
    content = RichTextField(blank=True, null=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
   #slug=models.SlugField(max_length=1000,null = True,blank =True)
    #image =models.ImageField(upload_to='imagees',null =True)
    created_at=models.DateTimeField(default=timezone.now)
    #upload_to=models.DateTimeField(default=timezone.now)
    date_posted= models.DateTimeField(default=timezone.now)
    #category= models.CharField(max_length=255,default='coding')
    snippet= models.CharField(max_length=800,default='Write a snippet for your post here!!')
    likes = models.ManyToManyField(User, related_name='blog_posts')
    class Meta:
        db_table = "post_data"

    # def total_likes(self):
    #     return self.likes.count()
    def __str__(self):
        return self.title + " Blog Title: " + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('blog-home')

    

# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     blog = models.ForeignKey(Post, on_delete=models.CASCADE)
#     parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
#     dateTime=models.DateTimeField(default=timezone.now)
 
#     def __str__(self):
#         return self.user.username +  " Comment: " + self.content

# class User(models.Model):  
#     uid = models.CharField(max_length=20)  
#     user_name = models.CharField(max_length=30)  
#     uemail = models.EmailField(max_length=100)  
#     ucontact = models.CharField(max_length=10)  
#     upwd = models.CharField(max_length=8)
#     class Meta:  
#         db_table = "user"  


