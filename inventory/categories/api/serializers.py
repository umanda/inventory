# -*- coding: utf-8 -*-
#
# inventory/categories/api/serializers.py
#

import logging

from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from inventory.common.api.serializer_mixin import SerializerMixin

from ..models import Category

log = logging.getLogger('api.categories.serializers')
User = get_user_model()


class CategorySerializer(SerializerMixin, serializers.ModelSerializer):

    owner = serializers.HyperlinkedRelatedField(
        view_name='user-detail', queryset=User.objects.all())
    parent = serializers.HyperlinkedRelatedField(
        view_name='category-detail', queryset=Category.objects.all(),
        default=None)
    uri = serializers.HyperlinkedIdentityField(
        view_name='category-detail')

    def validate(self, data):
        if not self.has_full_access():
            owner = data.get('owner')
            user = self.get_user_object()

            if owner.id != user.id:
                log.info("Owner PK: %s, request user PK: %s", owner.id, user.id)
                raise PermissionDenied(
                    detail=_("The owner for this record must be the same as "
                             "the user who is creating or altering the record.")
                    )

        return data

    def create(self, validated_data):
        user = self.get_user_object()
        validated_data['creator'] = user
        validated_data['updater'] = user
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.parent = validated_data.get('parent', instance.parent)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.updater = self.get_user_object()
        instance.save()
        return instance

    class Meta:
        model = Category
        fields = ('id', 'owner', 'name', 'parent', 'path', 'level', 'creator',
                  'created', 'updater', 'updated', 'uri',)
        read_only_fields = ('id', 'path', 'level', 'creator', 'created',
                            'updater', 'updated',)
        extra_kwargs = {'level': {'default': 0}}
