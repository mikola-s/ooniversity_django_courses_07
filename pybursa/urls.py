from django.conf.urls import url, include
from django.contrib import admin
from pybursa import views
from quadratic.views import quadratic_results

urlpatterns = [
    url(r'^quadratic/results/', quadratic_results, name="results"),
    url(r'^$', views.index, name="index"),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^student_list/', views.student_list, name="student_list"),
    url(r'^student_detail/', views.student_detail, name="student_detail"),
    url(r'^polls/', include("polls.urls")),
    url(r'^admin/', admin.site.urls),
]
