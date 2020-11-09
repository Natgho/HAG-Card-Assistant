# Create your views here.
from rest_framework import viewsets

from hagAsistantCard.serializers import ArticleSerializer
from restApi.models import Article
import django_filters.rest_framework


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Article.objects.all().order_by('article_id')
    serializer_class = ArticleSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['lang']
    http_method_names = ['get']
