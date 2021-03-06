# -*- coding: utf-8 -*-
#
# inventory/accounts/api/views.py
#

import logging

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from rest_condition import ConditionalPermission, C, And, Or, Not

from oauth2_provider.ext.rest_framework import (
    TokenHasReadWriteScope, TokenHasScope)

from inventory.common.api.permissions import (
    IsAdminSuperUser, IsAdministrator, IsProjectManager, IsAnyUser)
from inventory.common.api.pagination import SmallResultsSetPagination

from ..models import Question, Answer
from .serializers import (
    UserSerializer, GroupSerializer, QuestionSerializer, AnswerSerializer)

log = logging.getLogger('api.accounts.views')
User = get_user_model()


#
# User
#
class UserAuthorizationMixin(object):

    def get_queryset(self):
        result = []

        if (self.request.user.is_superuser or
            self.request.user.role == User.ADMINISTRATOR):
            result = User.objects.all()
        else:
            result[:] = [self.request.user]

        return result


class UserList(UserAuthorizationMixin, ListCreateAPIView):
    """
    User list endpoint.
    """
    serializer_class = UserSerializer
    permission_classes = (
        And(
            Or(IsAnyUser),#IsAdminSuperUser, IsAdministrator, IsProjectManager),
            Or(TokenHasReadWriteScope, IsAuthenticated)
            ),
        )
    pagination_class = SmallResultsSetPagination

user_list = UserList.as_view()


class UserDetail(UserAuthorizationMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = (
        And(
            Or(IsAnyUser),#IsAdminSuperUser, IsAdministrator, IsProjectManager),
            Or(TokenHasReadWriteScope, IsAuthenticated)
            ),
        )

user_detail = UserDetail.as_view()


#
# Group
#
class GroupAuthorizationMixin(object):

    def get_queryset(self):
        result = []

        if (self.request.user.is_superuser or
            self.request.user.role == User.ADMINISTRATOR):
            result = Group.objects.all()
        else:
            result = self.request.user.groups.all()

        return result


class GroupList(GroupAuthorizationMixin, ListCreateAPIView):
    """
    Group list endpoint.
    """
    serializer_class = GroupSerializer
    permission_classes = (
        And(
            Or(IsAnyUser),#IsAdminSuperUser, IsAdministrator, IsProjectManager),
            Or(TokenHasScope, IsAuthenticated)
            ),
        )
    required_scopes = ('read', 'write', 'groups',)
    pagination_class = SmallResultsSetPagination

group_list = GroupList.as_view()


class GroupDetail(GroupAuthorizationMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    permission_classes = (
        And(
            Or(IsAnyUser),#IsAdminSuperUser, IsAdministrator, IsProjectManager),
            Or(TokenHasScope, IsAuthenticated)
            ),
        )
    required_scopes = ('read', 'write', 'groups',)

group_detail = GroupDetail.as_view()


#
# Question
#
class QuestionAuthorizationMixin(object):

    def get_queryset(self):
        result = []

        if (self.request.user.is_superuser or
            self.request.user.role == User.ADMINISTRATOR):
            result = Question.objects.all()
        else:
            result = [answer.question
                      for answer in self.request.user.answers.all()]

        return result


class QuestionList(QuestionAuthorizationMixin, ListCreateAPIView):
    """
    Question list endpoint.
    """
    serializer_class = QuestionSerializer
    permission_classes = (
        And(IsAnyUser,
            Or(TokenHasReadWriteScope, IsAuthenticated)),
        )
    pagination_class = SmallResultsSetPagination

question_list = QuestionList.as_view()


class QuestionDetail(QuestionAuthorizationMixin, RetrieveUpdateDestroyAPIView):
    """
    Question detail endpoint.
    """
    permission_classes = (
        And(IsAnyUser,
            Or(TokenHasReadWriteScope, IsAuthenticated)),
        )
    serializer_class = QuestionSerializer

question_detail = QuestionDetail.as_view()


#
# Answer
#
class AnswerAuthorizationMixin(object):

    def get_queryset(self):
        result = []

        if (self.request.user.is_superuser or
            self.request.user.role == User.ADMINISTRATOR):
            result = Answer.objects.all()
        else:
            result = self.request.user.answers.all()

        return result


class AnswerList(AnswerAuthorizationMixin, ListCreateAPIView):
    """
    Answer list endpoint.
    """
    serializer_class = AnswerSerializer
    permission_classes = (
        And(IsAnyUser,
            Or(TokenHasReadWriteScope, IsAuthenticated)),
        )
    pagination_class = SmallResultsSetPagination

answer_list = AnswerList.as_view()


class AnswerDetail(AnswerAuthorizationMixin, RetrieveUpdateDestroyAPIView):
    """
    Answer detail endpoint.
    """
    permission_classes = (
        And(IsAnyUser,
            Or(TokenHasReadWriteScope, IsAuthenticated)),
        )
    serializer_class = AnswerSerializer

answer_detail = AnswerDetail.as_view()
