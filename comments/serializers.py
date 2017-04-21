from rest_framework import serializers


class CommentsListGetRequestSerializer(serializers.Serializer):
    object_id = serializers.UUIDField(required=True)
    p_no = serializers.IntegerField(required=False, default=1)


class CommentsListPostRequestSeriaizer(serializers.Serializer):
    object_id = serializers.UUIDField(required=True)
    content_type = serializers.UUIDField(required=True)
    subject = serializers.CharField(required=True)
    text = serializers.CharField(required=True)


class ErrorResponseSerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True)
    message = serializers.CharField(required=True, max_length=255)
    errors = serializers.ListField(required=True)
    debug = serializers.ListField(required=False)


class CommentSerializer(serializers.Serializer):
    """
        Change this to serve filter or add any filds in the returning Comment object
    """

    id = serializers.UUIDField()
    user_id = serializers.CharField()
    user_first_name = serializers.CharField()
    user_last_name = serializers.CharField()
    object_id = serializers.UUIDField()
    subject = serializers.CharField()
    text = serializers.CharField()
    created = serializers.DateTimeField()
