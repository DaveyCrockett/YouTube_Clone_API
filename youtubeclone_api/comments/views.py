from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class CommentList(APIView):

    def get(self, request):
        if request.method == 'GET':
            comments = Comment.objects.all()
            currentComments = request.query_params.get('currentComments', None)
            if currentComments is not None:
                comments = comments.filter(currentComments_icontains=currentComments)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

    def post(self, request):
        if request.method == 'POST':
            comment_data = JSONParser().parse(request)
            serializer = CommentSerializer(data=comment_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)