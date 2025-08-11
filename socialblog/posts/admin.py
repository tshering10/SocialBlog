from django.contrib import admin
from posts.models import Post, Like, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_at', 'updated_at']
    
admin.site.register(Post,PostAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'liked_time']
admin.site.register(Like, LikeAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','post', 'comment', 'created_at' ]
admin.site.register(Comment,CommentAdmin)