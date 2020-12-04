from django.urls import path
from .views import UserRegistrApiView,\
    UserLoginApiVIew,UseApiAuthView


urlpatterns=[
    path('',UserRegistrApiView.as_view()),
    path('login/', UserLoginApiVIew.as_view()),
    # path('api-auth/', UseApiAuthView.as_view())
]