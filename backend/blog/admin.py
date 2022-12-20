from django.contrib import admin

from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile


# admin.site.register(Profile, ProfileAdmin)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag


# admin.site.register(Tag, TagAdmin)

@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    model = Category

    list_display = (
        "id",
        "name",
        "subname",
        "slug",
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True
