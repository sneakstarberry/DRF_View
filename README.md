
```from post.models import Post```<br/>
```from post.serializer import PostSerializer```
<pre><code>
    from rest_framework.response import Response
    from rest_framework import status
    from rest_framework.views import APIView
    from django.shortcuts import get_object_or_404
<pre/><code/>

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

