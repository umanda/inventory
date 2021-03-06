#
# inventory/regions/api/views.py
#

import logging

from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from rest_condition import ConditionalPermission, C, And, Or, Not

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope

from inventory.common.api.permissions import (
    IsAdminSuperUser, IsAdministrator, IsProjectManager, IsAnyUser)
from inventory.common.api.pagination import SmallResultsSetPagination
from inventory.regions.models import Country, Region

from .serializers import RegionSerializer, CountrySerializer


log = logging.getLogger('api.regions.views')


#
# Country
#
class CountryList(ListCreateAPIView):
    """
    Country list endpoint.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (
        Or(IsAnyUser),# IsAdminSuperUser, IsAdministrator, IsProjectManager,),
        And(Or(TokenHasReadWriteScope, IsAuthenticated,),),
        )
    pagination_class = SmallResultsSetPagination

country_list = CountryList.as_view()


class CountryDetail(RetrieveUpdateDestroyAPIView):
    """
    Country detail endpoint.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (
        Or(IsAnyUser),#IsAdminSuperUser, IsAdministrator, IsProjectManager,),
        And(Or(TokenHasReadWriteScope, IsAuthenticated,),),
        )

country_detail = CountryDetail.as_view()


#
# Region
#
class RegionList(ListCreateAPIView):
    """
    Region list endpoint.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (
        Or(IsAnyUser),#IsAdminSuperUser, IsAdministrator, IsProjectManager,),
        And(Or(TokenHasReadWriteScope, IsAuthenticated,),),
        )
    pagination_class = SmallResultsSetPagination

region_list = RegionList.as_view()


class RegionDetail(RetrieveUpdateDestroyAPIView):
    """
    Region detail endpoint.
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (
        Or(IsAnyUser),#IsAdminSuperUser, IsAdministrator, IsProjectManager,),
        And(Or(TokenHasReadWriteScope, IsAuthenticated,),),
        )

region_detail = RegionDetail.as_view()
