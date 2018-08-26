from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, filters
from rest_framework.pagination import PageNumberPagination

from app01.filters import GoodsFilter
from app01.models import Goods
from app01.serializers import GoodsSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 10


# class GoodsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
class GoodsViewSet(viewsets.ModelViewSet):
    """
    List
        商品列表页,分页,搜索,排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'price')
    ordering_fields = ('name', 'price')
