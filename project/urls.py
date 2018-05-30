from django.conf.urls import url
from project import views


urlpatterns = [
    url(r'^index$', views.index,name='index'),
    url(r'^register$', views.register),
    url(r'^register_check$', views.register_check),
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^show_msg$', views.show_msg),
    url(r'^html_escape$', views.html_escape),
    url(r'^02$',views.zero_two,name='02'),
    url(r'^url_reverse$',views.url_reverse),
    url(r"^show_args/(\d+)/(\d+)$",views.show_args,name='show_args'),
    url(r"^show_kwargs/(?P<c>\d+)/(?P<d>\d+)$",views.show_kwargs,name='show_kwargs'),
    url(r'^test_rediret$',views.test_rediret),
    url(r'^page/(?P<pindex>[0-9]*)$',views.area),
    url(r'^area1$',views.area1),
    url(r'^area2$',views.area2),
    url(r'^area3_(\d+)$',views.area3),
]
