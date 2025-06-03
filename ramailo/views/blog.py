from rest_framework.decorators import api_view
from ramailo.models.blog import Post, Comment
from ramailo.serializers.blog_serializer import PostSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# @api_view(['POST'])
def create_blog(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
    return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
def get_all_blog(request):
    post = Post.objects.all()
    serializer = PostSerializer(post , many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data , content_type="application/json")

# @api_view(['GET'])
def get_blog(request , id):
    post = Post.objects.get(id= id)
    serializer = PostSerializer(post)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data , content_type="application/json")

# @api_view(['PUT'])
def update_blog(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
def delete_blog(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def posts_view(request):
    if request.method == 'GET':
        return get_all_blog(request)
    return create_blog(request)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail_view(request, id):
    if request.method == 'GET':
        return get_blog(request, id)
    elif request.method == 'PUT':
        return update_blog(request, id)
    elif request.method == 'DELETE':
        return delete_blog(request, id)
