# 데이터 처리 대상
from post.models import Post
from post.serializer import PostSerializer
# status에 따라 직접 Response를 처리할 것
from django.http import Http404 # Get Object or 404 직접 구현
# from django.shortcuts import get_object_or_404
# PostDetail 클래스의 get_object 메소드 대신 이거 써도 된다

class PostList(APIView):




class PostDetail(APIView):
