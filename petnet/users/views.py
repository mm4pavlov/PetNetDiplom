from .models import CustomUser, Post
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import viewsets
from .serializer import PostSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView



__all__ = [
    'Posts',
    'UsersPost'
]


class Posts(View):
    def get(self, request, user_id):
        if request.user.is_authenticated:
            posts = Post.objects.all()
            user = CustomUser.objects.get(id=user_id)
            return render(request, 'time-line.html', context={'user': user, 'posts': posts})
        return redirect('/')

    def post(self, request, user_id):
        Post.objects.create(
            author=CustomUser.objects.get(id=user_id),
            text=request.POST['text']
        )
        return self.get(request, user_id)


class UsersPost(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-post_dt')
    serializer_class = PostSerializer


class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
