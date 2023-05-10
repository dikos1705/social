from .serializers import UserSerializer
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from posts.models import Post

class UserAPIView(APIView):
    def get(self, request):
        u  = User.objects.all()
        print(u)
        return Response ({'users': UserSerializer(u,many=True).data})



# class UserfavAPIView(APIView):
#     def get(self, request,id):
#         post = Post.objects.get(id=<post_id>)
#         liked_users = post.likes.all().values_list('user__name', flat=True)
# #     # return user_liked_posts
#         print(user_liked_posts)
#         return Response({'users': user_liked_posts})
# def users_favourites(self, request):
#     print(request.user)
#     # user_liked_posts = Post.objects.filter(likes__user_id = user.id) 
#     # return user_liked_posts


from rest_framework import generics


class UserfavAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=request.user.id)
        liked_users = post.likes.all().values_list('user__name', flat=True)
        # liked_users = post.likes.all()
        serializer = self.get_serializer(liked_users, many=True)
        return Response(serializer.data)