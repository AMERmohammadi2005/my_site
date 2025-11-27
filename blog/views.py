from django.shortcuts import render , get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage , PageNotAnInteger
# Create your views here.

def blog_view(request , cat_name=None , author_username=None):
    posts = Post.objects.filter(status = 1 ,
                                 published_date__lte = timezone.now()
                                 ).order_by("-published_date")
    
    if cat_name :
        posts = posts.filter(category__name = cat_name)

    if author_username :
        posts = posts.filter(author__username = author_username)
    posts = Paginator(posts , 3)
    try:
       
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts =posts.get_page(1)

    except EmptyPage :
        posts.get_page(1)

    

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

def blog_category(request , cat_name):
    posts = Post.objects.filter(status = 1)
    posts = posts.filter(category__name = cat_name)

    context = {'posts':posts}

    return render(request ,"blog/blog-home.html",context )
    
def blog_search(request):
    posts = Post.objects.filter(status = 1 ,
                                 published_date__lte = timezone.now()
                                 ).order_by("-published_date")

    #print(request.__dict__)
    if request.method == 'GET':
        #print( request.GET.get('s'))
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)

    context = {'posts':posts}
    return render(request ,"blog/blog-home.html" , context )
 
