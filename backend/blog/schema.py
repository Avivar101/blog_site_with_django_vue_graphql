from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
import graphene

from blog import models


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile


class PostType(DjangoObjectType):
    class Meta:
        model = models.Post


class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag


class Query(graphene.ObjectType):
    all_post = graphene.List(PostType)
    author_by_username = graphene.Field(AuthorType, username=graphene.String())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    posts_by_author = graphene.List(PostType, username=graphene.String())
    posts_by_tag = graphene.List(PostType, tag=graphene.String())

    def resolve_all_posts(root, info):
        return (
            models.Post.objects.prefetch_related("tags")
            .selected_related("author")
            .all()
        )

    def resolve_author_by_username(root, info, username):
        return ()

    def resolve_post_by_slug(self):
        pass

    def resolve_posts_by_author(self):
        pass

    def resolve_posts_by_tag(self):
        pass