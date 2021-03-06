# -*- coding: utf-8 -*-
#
# inventory/regions/models.py
#

import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _

from inventory.common.model_mixins import (
    UserModelMixin, TimeModelMixin, StatusModelMixin, StatusModelManagerMixin)

log = logging.getLogger('inventory.regions.models')


#
# Country
#
class CountryManager(StatusModelManagerMixin, models.Manager):

    def get_regions_by_country(self, country, code=False):
        """
        Get the regions associated with the provided country.
        """
        query = []
        result = []

        if isinstance(country, (int, long)):
            if not code:
                query.append(models.Q(pk=country))
            else:
                query.append(models.Q(country_number_code=country))
        else:
            # Could just be luck, but couldn't find any country names
            # shorter that four characters.
            if len(country) == 2:
                query.append(models.Q(country_code_2=country))
            elif len(country) == 3:
                query.append(models.Q(country_code_3=country))
            else:
                query.append(models.Q(country=country))

        countries = self.filter(*query)

        if countries:
            if countries.count() > 1:
                log.error("Something is wrong, should only have one country "
                          "object, found: %s, country: %s, code: %s",
                          countries, country, code)

            result = countries[0].regions.all()

        return result


class Country(TimeModelMixin, UserModelMixin, StatusModelMixin):
    """
    This model implements country functionality.
    """
    country = models.CharField(
        verbose_name=_("Country"), max_length=100)
    country_code_2 = models.CharField(
        verbose_name=_("Country Code 2"), max_length=2, db_index=True,
        unique=True)
    country_code_3 = models.CharField(
        verbose_name=_("Country Code 3"), max_length=3, blank=True, null=True,
        db_index=True, unique=True)
    country_number_code = models.PositiveIntegerField(
        verbose_name=_("country Number Code"), default=0, blank=True,
        null=True)

    objects = CountryManager()

    class Meta:
        ordering = ('country',)
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def save(self, *args, **kwargs):
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return "{} ({})".format(self.country, self.country_code_2)


#
# Region
#
class RegionManager(StatusModelManagerMixin, models.Manager):
    pass


class Region(TimeModelMixin, UserModelMixin, StatusModelMixin):
    """
    This model implements region functionality.
    """
    country = models.ForeignKey(
        Country, verbose_name=_("Country"), related_name='regions')
    region_code = models.CharField(
        verbose_name=_("Region Code"), max_length=10, db_index=True)
    region = models.CharField(
        verbose_name=_("Region"), max_length=100)
    primary_level = models.CharField(
        verbose_name=_("Primary Level"), max_length=50, blank=True, null=True)

    objects = RegionManager()

    class Meta:
        unique_together = ('country', 'region',)
        ordering = ('region', 'region_code',)
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def save(self, *args, **kwargs):
        super(Region, self).save(*args, **kwargs)

    def __str__(self):
        return self.region
