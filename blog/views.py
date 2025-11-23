from django.shortcuts import render , get_object_or_404
from blog.models import Post
from django.utils import timezone
# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(status = 1 ,
                                 published_date__lte = timezone.now()
                                 ).order_by("-published_date")
    context = {'posts':posts}
    return render(request ,"blog/blog-home.html" , context )


def blog_single_view(request ,pid):
   
    posts = Post.objects.filter(status = 1 , published_date__lte = timezone.now())
    post = get_object_or_404(posts  , pk = pid ,)
    post.counted_view += 1
    post.save(update_fields=['counted_view'])

    posts_list = list(posts.order_by('id'))
    
    current_index = posts_list.index(post)
    next_post = posts_list[current_index + 1] if current_index + 1 < len(posts_list) else None
    prev_post = posts_list[current_index - 1] if current_index > 0 else None
    context = {'post':post,
               'prev_post' : prev_post,
                'next_post' :next_post }
    return render(request ,"blog/blog-single.html",context )

def test_view(request ):
  
    return render(request , "blog/test.html"  )

