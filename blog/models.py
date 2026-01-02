from django.db import models

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    



class Post(models.Model):
    titlle = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts", null=True)
    excerpt = models.TextField()
    date = models.DateField(auto_now=True)
    content = models.TextField()
    slug = models.SlugField(unique=True,db_index=True)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.titlle


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comments")

