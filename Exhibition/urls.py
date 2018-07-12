"""Exhibition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.views.static import serve
import xadmin

from users.views import LoginView, LogoutView, MessageView
from reservation.views import ReservationView, CheckView, RecordView
from .settings import STATIC_ROOT


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^$', CheckView.as_view(), name='index'),
    url(r'^reservation/', ReservationView.as_view(), name='reservation'),
    url(r'^record/', RecordView.as_view(), name='record'),
    url(r'^suggestion/', MessageView.as_view(), name='suggestion'),

    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT})

]

handler500 = 'users.views.page_not_found'