from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name =  models.CharField(max_length=255)
    


    def __str__(self):
        return self.name



class Post(models.Model) :
    author = models.ForeignKey(User , on_delete = models.SET_NULL, null=True  )
    image = models.ImageField(upload_to='blog/' , default='blog/default.jpg') 
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tag 
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default= 0)
    status = models.BooleanField(default= False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    
    def __str__(self):
        return f"{self.title}"
    
    #def snippets(self):
    #    return self.content[:100]+"..."
    
    class Meta:
        ordering = ['-created_date' , ]
 
