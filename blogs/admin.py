from django.contrib import admin
from .models import Blogs, categories, Rating
# Register your models here.
class categoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
admin.site.register(categories, categoriesAdmin)
admin.site.register(Blogs)
admin.site.register(Rating)
