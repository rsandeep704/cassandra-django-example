from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
import datetime, uuid


class Comment(Model):
    """
    Class that represents a user comment
    """

    id = columns.UUID(primary_key=True, partition_key=True, index=True, default=uuid.uuid4)
    user_id = columns.UUID(primary_key=True, partition_key=True, index=True, required=True)
    user_first_name = columns.Text()
    user_last_name = columns.Text()
    content_type = columns.UUID()  # use to form the URL of the object
    object_id = columns.UUID(primary_key=True, partition_key=True, index=True, required=True)
    subject = columns.Text(max_length=256)
    text = columns.Text(required=True, max_length=2048)
    created = columns.DateTime(required=True, default=datetime.datetime.now())  # TODO: Handle timezone
    last_modified = columns.DateTime(required=True, default=datetime.datetime.now())
    is_removed = columns.Boolean(default=False, partition_key=True)

    @classmethod
    def get_comments_for_obj(cls, object_id, p_no=1):
        # implement pagination
        comments = cls.objects.filter(object_id=object_id)
        return comments

    @classmethod
    def create(cls, **data):
        comment = Comment(**data)
        comment.save()
        return comment


class ErrorResponse():
    """
    The response in case of an error
    """

    def __init__(self, **kwargs):
        self.code = kwargs.get('code', 500)
        self.message = kwargs.get('message', "Internal Server Error")
        self.debug = kwargs.get('debug', None)
        self.errors = kwargs.get('errors', [])
