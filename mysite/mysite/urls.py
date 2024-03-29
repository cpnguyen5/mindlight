"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from dashing import utils
from dashing.utils import router
from django.views.generic.base import RedirectView
from .widgets import CustomWidget

router.register(CustomWidget, 'custom_widget', eg_kwargs_param="[A-Za-z0-9_-]+")

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', include(router.urls)),
    url(r'^$', RedirectView.as_view(url='dashboard/'), name='index'),
    #url(r'^simple_chart/$', include(templatespolls.site.simple_chart, name="simple_chart"),

#    url(r'^dashboard/', include('dashing.urls')),

]
#    url(r'^dashboard/', include(router.urls)),

