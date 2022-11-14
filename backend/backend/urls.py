from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView


urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/index.html'),),
    path('admin/', admin.site.urls),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True),)),
    path('accounts/', include('allauth.urls')),
]
