
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaoftriangle/',views.trianglearea,name="areaoftriangle"),
    path('',views.trianglearea,name="areaoftriangleroot")
]