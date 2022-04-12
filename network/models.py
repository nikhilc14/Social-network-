from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass 

class click(models.Model):
    user = models.ForeignKey("User",on_delete=models.CASCADE)
    icon_clicked = models.BooleanField(blank=True,null=True,default=False)
    post_clicked = models.ManyToManyField("posts",related_name="likes_of_post",blank=True)

    def __str__(self):
        return f"{self.user}"



class posts(models.Model):
    user = models.ForeignKey("User",on_delete=models.CASCADE)
    post = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(null=True,default=0)
    liked = models.ManyToManyField(User,related_name="user_likes",blank=True)

    def __str__(self):
        return f"{self.post}"

    def serialize(self):
        return {
            "id":self.id,
            "user":self.user,
            "post":self.post,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")
        }
    
class followings (models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE,default=1)
    following = models.ManyToManyField(User,related_name="followers")

    def __str__(self):
        return f"{self.user}"