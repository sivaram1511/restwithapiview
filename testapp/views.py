from django.shortcuts import render
from rest_framework.response import Response
from testapp.pagination import MyPagination,MyPagination2,MyPagination3
from testapp import serializers
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.
class EmployeeListApiView(APIView):
    def get(self,request,format=None):
        a=set()
        qs=Employee.objects.all().order_by('esal')
        for i in qs:
            a.add(i.esal)
        data=sorted(a,reverse=True)
        print(data)
        xy=Employee.objects.filter(esal=data[1])
        serializer=EmployeeSerializer(xy,many=True)

        return Response(serializer.data)
class EmployeeApiView(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    #pagination_class=MyPagination2
    pagination_class=MyPagination3




#class EmployeeCreateAPIView(CreateAPIView):
   # queryset = Employee.objects.all()
    #serializer_class = EmployeeSerializer
#class EmployeeRetrieveAPIView(RetrieveAPIView):
   # queryset=Employee.objects.all()
   # serializer_class=EmployeeSerializer
    #lookup_field="id"

#class EmployeeCreateApiView(CreateAPIView):
 #   queryset=Employee.objects.all()
 #   serializer_class=EmployeeSerializer
#class EmployeeRetrieveApiView(RetrieveAPIView):
 #   queryset=Employee.objects.all()
  #  serializer_class = EmployeeSerializer
  #  lookup_field = 'id'
#class EmployeeUpdateApiView(UpdateAPIView):
 #  queryset = Employee.objects.all()
 #  serializer_class=EmployeeSerializer
 #  lookup_field = 'id'
#class EmployeeDestroyAPIView(DestroyAPIView):
 #   queryset=Employee.objects.all()
 #   serializer_class=EmployeeSerializer
  #  lookup_field="id"
class EmployeeListCreateApiView(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'
#class EmployeeRetrieveUpdateApiView(RetrieveUpdateAPIView):
    #serializer_class=EmployeeSerializer
    #lookup_field='id'
#class EmployeeRetrieveDestroyApiView(RetrieveDestroyAPIView):
   # serializer_class = EmployeeSerializer
   # queryset = Employee.objects.all()
    #lookup_field='id'

