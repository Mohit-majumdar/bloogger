from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    User=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=100,null=True)
    subtitle=models.CharField(max_length=50,null=True)
    image=models.FileField(null=True)
    date=models.DateField(null=True)
    discription = models.CharField(max_length=400,null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, null=True)
    comment = models.TextField(null=True)


    def __str__(self):
        return self.post.title
class Post_like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    like = models.IntegerField(null=True)
    def __str__(self):
        return self.post.title + "---" + str(self.like)


