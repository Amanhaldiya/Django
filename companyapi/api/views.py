from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.rest import Companyrest,Employeerest
from rest_framework.decorators import action


from rest_framework.response import Response

# Create your views here.




class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=Companyrest
#companies/{companyId}/employees
#function to get particular company employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
           print("Get employees of",pk,"company")
           company=Company.objects.get(pk=pk)
           emps=Employee.objects.filter(company=company)
           emps_rest=Employeerest(emps,many=True,context={'request':request})
           return Response(emps_rest.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'company might not exist !! error'
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Employeerest
