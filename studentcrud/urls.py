"""
URL configuration for modelviewset project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from application1 import views
from rest_framework.routers import DefaultRouter
#creating router object
router = DefaultRouter()
from application1.views import studentModelViewSet

#Register studentviewset with router
router.register('studentapi',views.studentModelViewSet,basename='studentmodelviewset')

# snippet_list = studentModelViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = studentModelViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

urlpatterns = [
    path('admin/', admin.site.urls),
    # # path('student/student', include(router.urls)),
    path('student/getallstudent', studentModelViewSet.as_view({'get':'list'})),
    path('student/addstudent', studentModelViewSet.as_view({'post': 'create'})),
    path('student/getstudentbyid/<int:pk>', studentModelViewSet.as_view({'get':'retrieve'})),
    path('student/updatestudent/<int:pk>', studentModelViewSet.as_view({'put': 'update'})),
    path('student/partialupdatestudent/<int:pk>', studentModelViewSet.as_view({'patch': 'partial_update'})),
    path('student/deletestudentbyid/<int:pk>', studentModelViewSet.as_view({'delete': 'destroy'})),


]
