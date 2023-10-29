from django.urls import path
from . import views
from .views import AddPostView , ArticleDetailView , HomeView, UpdatePostView, DeletePostView
urlpatterns = [
   
    #path("home/", views.home,name="blog-home"),
    path("home/", HomeView.as_view(),name="blog-home"),
    path("addblog/", views.AddPostView,name="add-blog"),
    #path("addcategory/", AddCategoryView.as_view(),name="add-category"),
    #path("login/", views.Login,name="blog-login"),
    path("base/", views.base),
    # path("register/", views.register,name="blog-register"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/remove<int:pk>', DeletePostView.as_view(), name="delete_post"),
    # path('like/<int:pk>', views.LikeView, name='like_post'),
]


