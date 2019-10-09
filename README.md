## API_View
<pre><code>
from post.models import Post
from post.serializer import PostSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True) 
        return Response(serializer.data) 

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():  
            serializer.save()       
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# PostList 클래스와는 달리 pk값을 받음 (메소드에 pk인자)
class PostDetail(APIView):

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        # post = get_object_or_404(Post, pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
</pre></code>
<hr/>

## Mixin_View
mixin 직접 보기 : <https://github.com/encode/django-rest-framework/blob/master/rest_framework/mixins.py>
genericAPIView 직접 보기 : <https://github.com/encode/django-rest-framework/blob/master/rest_framework/generics.py>
<pre><code>
# 데이터 처리 대상 : 모델, Serializer import 시키기
from post.models import Post
from post.serializer import PostSerializer

from rest_framework import generics
from rest_framework import mixins



class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, 
                generics.GenericAPIView):
    queryset = Post.objects.all()   # 쿼리셋 등록!
    serializer_class = PostSerializer # Serializer 클래스 등록!

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

</pre></code>
