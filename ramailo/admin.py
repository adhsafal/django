from django.contrib import admin

from ramailo.models.feedback import Feedback
from ramailo.models.notification import FCMDevice
from ramailo.models.user import User
from ramailo.models.blog import Post, Comment, Category, PostImage


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'idx', 'mobile', 'name', 'position', 'created_at']
    search_fields = ['name', 'mobile']
    list_filter = ['is_approved', 'is_email_verified', 'is_kyc_verified']


admin.site.register(FCMDevice)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'is_published', 'created_at']
    search_fields = ['title', 'author']
    list_filter = ['is_published', 'categories']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'content', 'created_at']
    search_fields = ['post__title', 'user__name']
    list_filter = ['created_at']
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'url', 'created_at']
    search_fields = ['post__title', 'url']
    list_filter = ['created_at']
    

