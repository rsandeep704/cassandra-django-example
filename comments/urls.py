from django.conf.urls import url

from .views import CommentListView

urlpatterns = [
    url('$', CommentListView.as_view(), name='comments_list')
]
