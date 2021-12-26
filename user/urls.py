from django.urls import path,include
from . import views

urlpatterns=[
    path('UserCreate',views.UserCreateView.as_view()),
    path('TwitterCreate',views.TwitterCreateView.as_view()),
    # path('getTwitter',views.TwitterGet.as_view())
    path('Data',views.GetData.as_view()),
]