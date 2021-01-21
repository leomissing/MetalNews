from django.urls import path, include
from Metal import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('news/',  views.news, name='news'),
    path('post/<id>/', views.post, name='post'),
    path('news/create/<id>', views.post_create, name='post_create'),
    path('post/delete/<id>', views.post_delete, name='post_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.RegisterFormView.as_view(), name='singup'),
    path('category/<id>', views.news_by_category, name='news_by_category')
]
