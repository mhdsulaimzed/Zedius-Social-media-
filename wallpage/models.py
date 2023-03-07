from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    profile_pic=models.ImageField(upload_to="images",null=True,blank=True)
    bio=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profiles")
    dob=models.DateField(null=True)
    city=models.CharField(max_length=50,null=True)
    followers=models.ManyToManyField(User,blank=True,related_name='followers')
    

    
    
    def __str__(self): 
        return self.user 

class Post(models.Model):
    image=models.ImageField(upload_to="images", null=True,blank=True)
    caption=models.CharField(max_length=60)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User,blank=True,related_name="likepost")
    @property 
    def like_count(self):
        cnt=self.likes.all().count()
        return cnt
    @property
    def post_comment(self):
        return Comment.objects.filter(post=self)
    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()
        
        
        


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    added_date=models.DateField(auto_now_add=True)
    body=models.CharField(max_length=60)
    likes=models.ManyToManyField(User,blank=True,related_name="likecomt")
    replies=models.ForeignKey('self', on_delete=models.CASCADE, null=True,related_name="comtreply")

    @property 
    def clike_count(self):
        cnt=self.likes.all().count()
        return cnt

# class Follow(models.Model):
#     follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
#     following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('follower', 'following')

        

    
   

    
    


    

