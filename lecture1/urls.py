from django.urls import path
from . import views

app_name = "lecture1"

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('', views.home, name='index'),
    path('hello/<str:name>', views.hello, name='hello'),
]