from django.contrib import admin

# Register your models here.

from .models import Author,Tag,Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author","date","tag",)
    list_display = ("titlle","author","date",)
    prepopulated_fields = {"slug":("titlle",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name","post")

admin.site.register(Author)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)