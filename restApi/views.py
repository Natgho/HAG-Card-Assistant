# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from hagAsistantCard.serializers import ArticleSerializer
from restApi.models import Articles


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Articles.objects.all().order_by('article_id')
    serializer_class = ArticleSerializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'lang'
    http_method_names = ['get']
