from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED

from .models import Comment, ErrorResponse
from .serializers import CommentsListGetRequestSerializer, CommentsListPostRequestSeriaizer, ErrorResponseSerializer, \
    CommentSerializer


class CommentListView(APIView):
    class CommentsListView(APIView):
        """
            View to handle lists of comments
        """

        # authentication_classes = (CommentRequestAuthentication,)

        def get(self, request):
            """
            :param request: HTTP get request
            :return: list of comments based on request imput params in quesry string
            """

            print(request.user) # works only if you have written an authentication class

            data = request.query_params
            debug = []

            request_data_serializer = CommentsListGetRequestSerializer(data=data)

            if not request_data_serializer.is_valid():
                error_response = ErrorResponse(errors=request_data_serializer.errors, code=HTTP_400_BAD_REQUEST,
                                               debug=debug)
                response_serializer = ErrorResponseSerializer(error_response)
                return Response(response_serializer.data, status=HTTP_400_BAD_REQUEST)

            data = request_data_serializer.data

            comments = Comment.get_comments_for_obj(object_id=data['object_id'], p_no=data['p_no'])
            comments_serializer = CommentSerializer(comments, many=True)

            return Response(comments_serializer.data)

        def post(self, request):
            """

            :param request: POST request to post a new comment
            :return: HTTP response cddes : 201 - created successfully, 400 - bad request
            """
            debug = []
            data = request.data
            request_data_serializer = CommentsListPostRequestSeriaizer(data=data)

            if not request_data_serializer.is_valid():
                error_response = ErrorResponse(errors=request_data_serializer.errors, code=HTTP_400_BAD_REQUEST,
                                               debug=debug)
                response_serializer = ErrorResponseSerializer(error_response)
                return Response(response_serializer.data, status=HTTP_400_BAD_REQUEST)

            data = request_data_serializer.data

            user_info = request.user  # works only if you have written an authentication class

            data.update(user_info)

            comment = Comment.create(data)

            status = HTTP_201_CREATED

            return Response(status=status)
