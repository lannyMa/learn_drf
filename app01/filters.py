#!/usr/bin/env python
# coding=utf-8
import django_filters

from app01.models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['name', 'min_price', 'max_price']
