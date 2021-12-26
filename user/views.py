from user.models import Twitter,User
from rest_framework.generics  import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserOrganisationSerializer,TwitterSerializer,ViewTwitterSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.permissions import IsAuthenticated
from functools import lru_cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.auth.hashers import make_password
from rest_framework import permissions
from django.views.decorators.cache import cache_page
# from lru.lrucache import LRUCache
# from lru_cache import LruCache

# Create your views here.
class UserCreateView(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class=UserOrganisationSerializer
    def post(self,request,format="json"):
        serializer=UserOrganisationSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(email=request.data['email'],name=request.data['name'],password = make_password(request.data['password']),is_manager=request.data['is_manager']) 
        else:
            return Response("User already exists",status=status.HTTP_404_NOT_FOUND)
        return Response({"Message":"Created","Data":serializer.data},status=status.HTTP_201_CREATED)

class TwitterCreateView(GenericAPIView):
    serializer_class=  TwitterSerializer
    def post(self,request,format="json"):
        serializer= TwitterSerializer(data=request.data)
        if serializer.is_valid():
            print(request.user.id)
            user_name=User.objects.filter(id=request.user.id).values_list("name")
            print(user_name[0][0])
            twitter = Twitter.objects.create(tweet=request.data['tweet'],name=user_name[0][0]) 
        return Response({"Message":"Created","Data":request.user.id},status=status.HTTP_201_CREATED)

# class TwitterGet(GenericAPIView):
#     # @lru_cache(maxsize=)
#     test = lru_cache(2)
#     authentication_classes = ()
#     permission_classes = ()
#     serializer=ViewTwitterSerializer
#     # @method_decorator(cache_page(60*60*2))
#     def get(self,request,format="json"):
#         data=Twitter.objects.values_list('name','tweet')
#         print(data)
#         test.cache_clear()
#         # Details = ViewTwitterSerializer(data,many=True)
#         return Response("ok",status=status.HTTP_200_OK)

# cache_page(10)
lru_cache(maxsize=10)
class GetData(GenericAPIView):
    # test = LRUCache(2)
    authentication_classes = ()
    permission_classes = ()
    serializer=ViewTwitterSerializer
    # @lru_cache(maxsize=2)
    def get(self,request,format="json"):
        data=Twitter.objects.all()
        Details = ViewTwitterSerializer(data,many=True)
        return Response(Details.data,status=status.HTTP_200_OK)