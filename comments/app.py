from django.apps import AppConfig
from cassandra.cqlengine import connection
from django.conf import settings


def setup_comments_db():
    hosts = settings.COMMENTS_CONFIG.get('cassandra_hosts', ['127.0.0.1'])
    keyspace = settings.COMMENTS_CONFIG.get('cassandra_keyspace', None)
    try:
        connection.setup(hosts=hosts, default_keyspace=keyspace, retry_connect=True)
    except Exception as e:
        print(e)
        # send a shut down signal and shutdown the server


class CommentsAppConfig(AppConfig):
    name = "comments"

    def ready(self):
        print("Setting up Connection ...")
        setup_comments_db()
        # do tasks to setup comments app
