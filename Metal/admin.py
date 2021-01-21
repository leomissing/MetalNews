from django.contrib import admin

from .models import Post, Category, Comments


class PostInstanceInline(admin.TabularInline):
    model = Comments


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'data', 'category']
    list_display_links = ['__str__','category']
    list_filter = ['data', 'category']
    search_fields = ['title', 'text']
    inlines = [PostInstanceInline]

    class Meta:
        model = Post


class CommentsModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'comment_post', 'data']
    list_display_links = ['comment_post']
    list_filter = ['comment_author', 'comment_post']
    search_fields = ['comment_post', 'comment_author']

    class Meta:
        model = Comments


admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)
admin.site.register(Comments, CommentsModelAdmin)
