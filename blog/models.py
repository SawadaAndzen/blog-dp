from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    
    def __str__(self):
        
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        
        return self.title
    
    def published_recently():
        ...