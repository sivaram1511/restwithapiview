"""restwithapiview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/',views.EmployeeListApiView.as_view()),
    path('api/',views.EmployeeApiView.as_view()),
    #path('api/',views.EmployeeCreateAPIView.as_view()),
    #path('api/<id>',views.EmployeeRetrieveAPIView.as_view()),
    #path('api/',views.EmployeeCreateApiView.as_view()),
    #path('api/<id>',views.EmployeeRetrieveApiView.as_view()),
    #path('api/<id>',views.EmployeeUpdateApiView.as_view()),
    #path('api/<id>',views.EmployeeDestroyAPIView.as_view()),
    path('api/$',views.EmployeeListCreateApiView.as_view()),
    path("api/<id>",views.EmployeeRetrieveUpdateDestroyApiView.as_view()),
   #path('api/<id>',views.EmployeeRetrieveUpdateApiView.as_view()),
    #path("api/<id>",views.EmployeeRetrieveDestroyApiView.as_view())
]
