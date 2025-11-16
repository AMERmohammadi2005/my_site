from django.urls import path 
from blog.views import *

app_name = "blog"

urlpatterns = [
    path("" , blog_view ,name='blog'),
    path("single/" , blog_single_view ,name='blog_single'),
    path("post-<int:pid>" ,test_view , name ='test'  )

]
