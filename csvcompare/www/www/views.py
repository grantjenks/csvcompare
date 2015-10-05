import csv
from cStringIO import StringIO

from rest_framework import viewsets, renderers, generics
from rest_framework.response import Response

from .models import Diff
from .serializers import DiffSerializer

from csvcompare import csv_file_diff, html

class DiffViewSet(viewsets.ModelViewSet):
    queryset = Diff.objects.all().order_by('-created')
    serializer_class = DiffSerializer

class DiffShow(generics.GenericAPIView):
    queryset = Diff.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        diff = self.get_object()

        old_cells = list(csv.reader(StringIO(diff.old)))
        new_cells = list(csv.reader(StringIO(diff.new)))

        return Response(html(csv_file_diff(old_cells, new_cells)))
