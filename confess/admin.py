from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
	date_hierarchy = "posted"
	fields = ("title", "text","image",'slug','total_likes','category')
	list_display = ["title", "posted","total_likes"]
	list_display_links = ["title"]
	list_filter = ["title"]
	search_fields = ["title"]
	

# Registrando la aplicacion Blog
admin.site.register(Post, PostAdmin)
# Register your models here.
