from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import status


@api_view(['GET'])
def api_preview(request):
    api = {
        'Post API': ['/api/post', '/api/post/<link>'],
        'Media API': ['/api/media'],
    }
    return Response(api)


@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == "GET":
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, link):
    try:
        post = get_object_or_404(Post, link=link)
    except Post.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PostSerializer(post, many=False, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        post.delete()
        return Response(status.HTTP_204_NO_CONTENT)
