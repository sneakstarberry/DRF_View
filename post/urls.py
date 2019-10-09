from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from post import views
# from rest_framework.routers import DefaultRouter

# Default Router 사용 X ==> API ROOT 없음. 

urlpatterns = [
    # 127.0.0.1:8000/post == ListView
    path('post/', views.PostList.as_view()),  
    # 127.0.0.1:8000/post/<pk> == DetailView
    path('post/<int:pk>/', views.PostDetail.as_view()), 
]

#
urlpatterns = format_suffix_patterns(urlpatterns)

# router = DefaultRouter()
# router.register('post', views.PostViewSet)

# urlpatterns = [
#     path('', include(router.urls))
# ]

