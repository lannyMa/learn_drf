#!/usr/bin/env python
# coding=utf-8
from rest_framework import serializers

from app01.models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        # fields = ('id', 'name', 'image', 'add_time')
        fields = '__all__'
