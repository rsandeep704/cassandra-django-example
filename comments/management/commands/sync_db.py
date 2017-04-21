import inspect
import comments.models as models_module
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import ModelMetaClass

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        for name, obj in inspect.getmembers(models_module):
            if inspect.isclass(obj) and type(obj) is ModelMetaClass:
                sync_table(obj)
