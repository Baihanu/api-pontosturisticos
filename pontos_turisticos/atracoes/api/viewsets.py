from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.atracoes.api.serializers import RecursoSerializer
from pontos_turisticos.atracoes.models import Recurso


class RecursoViewSet(ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer
