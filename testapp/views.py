from django.shortcuts import render
from rest_framework.response import Response

from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView
# Create your views here.
#class EmployeeListApiView(APIView):
    #def get(self,request,format=None):
      #  qs=Employee.objects.all()
       # serializer=EmployeeSerializer(qs,many=True)
       # return Response(serializer.data)
#class EmployeeApiView(ListAPIView):
    #serializer_class = EmployeeSerializer
    #def get_queryset(self):
       # qs=Employee.objects.all()
       # name=self.request.GET.get("ename")
       # if name is not None:
        #    qs=qs.filter(ename__icontains=name)
        #return qs
#class EmployeeCreateAPIView(CreateAPIView):
   # queryset = Employee.objects.all()
    #serializer_class = EmployeeSerializer
class EmployeeRetrieveAPIView(RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field="id"

#class EmployeeCreateApiView(CreateAPIView):
 #   queryset=Employee.objects.all()
 #   serializer_class=EmployeeSerializer
#class EmployeeRetrieveApiView(RetrieveAPIView):
 #   queryset=Employee.objects.all()
  #  serializer_class = EmployeeSerializer
  #  lookup_field = 'id'
#class EmployeeUpdateApiView(UpdateAPIView):
 #   queryset = Employee.objects.all()
  #  serializer_class=EmployeeSerializer
  #  lookup_field = 'id'
