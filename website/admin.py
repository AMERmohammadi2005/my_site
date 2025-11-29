from django.contrib import admin
from website.models import Contact , Newsletter

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["name","email","subject","created_date"]
    list_filter = ["email",]
    search_fields = ["name","massage",]



admin.site.register(Contact , ContactAdmin)

class NewsletterAdmin(admin.ModelAdmin):

   
    list_display = ["email",]
    list_filter = ["email",]

admin.site.register(Newsletter , NewsletterAdmin)
