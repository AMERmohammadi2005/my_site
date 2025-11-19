from django.contrib import admin
from blog.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = " null"
    list_display = ["title","counted_view","author","status",
                     "created_date","published_date" ]
    list_filter = ('status','author')
    ordering = ["-created_date"]
    search_fields = ['title','content']
    
#admin.site.register(Post , PostAdmin)
#line 5 and 9 do same thing in django