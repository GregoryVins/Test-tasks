from rest_framework.viewsets import ModelViewSet

from subdivisions.models import Subdivision
from subdivisions.serializers import SubdivisionSerializer


class SubdivisionViewSet(ModelViewSet):
    serializer_class = SubdivisionSerializer
    queryset = Subdivision.objects.all()
