#
# items/urls.py
#
# SVN/CVS Keywords
#----------------------------------
# $Author: cnobile $
# $Date: 2014-01-16 21:17:19 -0500 (Thu, 16 Jan 2014) $
# $Revision: 87 $
#----------------------------------

from django.conf.urls import include, url

from inventory.apps.items import views


urlpatterns = [
    url(r'^$', views.frontPage),
    #url(r'^lookup/regions/', views.processRegion),
    ]
