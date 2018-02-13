from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from Discussion.serializers import  *
from django.views.decorators.csrf import csrf_exempt
from Discussion.models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Create your views here.


@csrf_exempt
@api_view(['POST'])
def user_login(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 1. Get all discussions which type is Either Article or Question
# @csrf_exempt
# @api_view(['GET'])
# def discussions_list(request):
#     discussion_list =[]
#     discussions = Discussion.objects.filter(discussion_type__in=['article','question'])
#     serializer = DiscussionSerializer(discussions, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

class discussions_list(APIView):
	def get(self, request, format=None):
		discussions = Discussion.objects.filter(discussion_type__in = ['article', 'question'])
		serializer = DiscussionSerializer(discussions, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

# 2. Add comment api 
#    notes:only logged in user can add comment
#          one user can not add more than 1 comment in particular discussion
#          user can not comment on his own created discussion
# @csrf_exempt
# @api_view(['POST'])
# @authentication_classes((TokenAuthentication,))
# def comment_create(request):
#     if request.user.is_authenticated():
        
#         discussionid = request.data['discussion']
#         res = Discussion.objects.get(id = discussionid)
#         userlist = User.objects.all()
#         result = Discussion.objects.filter(added_by = request.user)

        
#         d_id = request.data['discussion']
#         comment = Comment.objects.all().filter(discussion = discussionid, added_by = request.user).exists()
#         if comment == True:
#             return Response({'error' : 'You already commented earlier in this Discussion.'}, status=status.HTTP_200_OK)
#         else:
#             if res in result:
#                 return Response({'error' : 'You can not comment on your Discussion'}, status=status.HTTP_200_OK)
#             else:
#                 serializer = CommentSerializer(data = request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data, status=status.HTTP_201_CREATED)
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)

@authentication_classes((TokenAuthentication,))
class comment_create(APIView):
	# authentication_classes = (TokenAuthentication,)
	# permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		print request.user
		if request.user.is_authenticated():
			owner = request.user
			data = request.data
			data['added_by'] = owner.id
			serializer = CommentSerializer(data=data)
			if serializer.is_valid():
				discussion_id = request.data['discussion']
				comment = Comment.objects.all().filter(discussion=discussion_id, added_by=owner.id).exists()
				if comment == True:
					return Response({'error': 'You already commented on this Discussion.'}, status=status.HTTP_200_OK)
				else:
					obj = Discussion.objects.get(id=discussion_id)
					dis_list = Comment.objects.filter(added_by=owner.id)
					print obj
					print dis_list
					if obj in dis_list:
						return Response({'error': 'You can not comment on your own Discussion.'}, status=status.HTTP_200_OK)
					else:
						serializer.save()
						return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)

# 3. Get all discussions which title matches searched term
#   example: /api/discussion/list/?title=Sports
# @api_view(['GET'])
# def discussions_Searchlist(request):
#     serializer = validateDiscssionSearchListSerializer(data=request.GET)
#     if serializer.is_valid():
#         try:
#             title = serializer.validated_data['title']
#             search_detail = Discussion.objects.filter(title__icontains=title)
#             data = DiscssionSearchListSerializer(search_detail, many=True)
#             return Response(data.data, status=status.HTTP_200_OK)
#         except:
#             return Response({'error': 'Discussion is not found'}, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class discussions_Searchlist(APIView):
    def get(self, request, format=None):
		title = request.GET.get('title')
		text = request.GET.get('text')
		discussion_type = request.GET.get('discussion_type')
		print title
		print text
		print discussion_type 
		search_detail = Discussion.objects.filter(title__icontains=title,text__icontains = text,discussion_type__icontains = discussion_type)
		data = DiscssionSearchListSerializer(search_detail, many=True)
		return Response(data.data, status=status.HTTP_200_OK)

        


# def DiscussionListSearch(request,title):
#     print title
#     try:
#         discussion = Discussion.objects.filter(Q(title__contains=title) | Q(text__contains=title))
#         print discussion
#     except:
#         import traceback
#         print traceback.print_exc()
#         return Response({'error': 'discussion id not found'}, status=status.HTTP_400_BAD_REQUEST)

#     serializer = DiscussionListSerializer(discussion, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

   
