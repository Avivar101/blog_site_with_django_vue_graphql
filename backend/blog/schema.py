from django.contrib.auth import get_user_model
from django.contrib.auth import models
from graphene_django import DjangoObjectType
import graphene
from datetime import datetime

from .models import *


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class AuthorType(DjangoObjectType):
    class Meta:
        model = Profile


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class CatType(DjangoObjectType):
    class Meta:
        model = Category


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="hello")
    all_posts = graphene.List(PostType)
    author_by_username = graphene.Field(AuthorType, username=graphene.String())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    posts_by_author = graphene.List(PostType, username=graphene.String())
    posts_by_tag = graphene.List(PostType, tag=graphene.String())
    categories = graphene.List(CatType)

    def resolve_all_posts(root, info):
        return (
            Post.objects.prefetch_related("tags")
                .select_related("author")
                .all()
        )

    def resolve_author_by_username(root, info, username):
        return Profile.objects.select_related("user").get(
            user__username=username
        )

    def resolve_post_by_slug(root, info, slug):
        return (
            Post.objects.prefetch_related("tags")
                .select_related("author")
                .get(slug=slug)
        )

    def resolve_posts_by_author(root, info, username):
        return (Post.objects.prefetch_related("tags")
                .select_related("author")
                .filter(author__user__username=username)
                )

    def resolve_posts_by_tag(root, info, tag):
        return (
            Post.objects.prefetch_related("tags")
                .select_related("author")
                .filter(tags__name__iexact=tag)
        )

    def resolve_categories(root, info):
        return (Category.objects.all())


class TagMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    tag = graphene.Field(TagType)

    @classmethod
    def mutate(cls, root, info, name):
        tag = Tag.objects.create(name=name)
        tag.save()
        return TagMutation(tag=tag)


class CatMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        subname = graphene.String()
        slug = graphene.String()
        body = graphene.String()
        publish_date = graphene.Date()

    cat = graphene.Field(CatType)

    @classmethod
    def mutate(cls, root, info, **args):
        cat = Category(
            name=args.get("name"),
            subname=args.get("subname"),
            slug=args.get("slug"),
            body=args.get("body"),
            publish_date=datetime.now(),
            author=Category.author
        )
        print(Category.author)
        cat.save()
        return CatMutation(cat=cat)


class Mutation(graphene.ObjectType):
    add_tags = TagMutation.Field()
    add_cats = CatMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
