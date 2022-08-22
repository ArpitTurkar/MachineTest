from sys import flags
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


# Create your views here.
class EmployeeView(APIView):
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'msg':'Employee added Successfully.'},status = status.HTTP_201_CREATED)

    def get(self, request, id=None, fname=None):
        print(fname,'------------------')
        if id is not None:
            try:
                employee_data = Employee.objects.get(id = id)   
                serializer = self.serializer_class(employee_data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({'msg':'Id does not exists!'}, status=status.HTTP_400_BAD_REQUEST)

        if fname is not None:
            all_emp = Employee.objects.filter(emp_fname__contains = fname)
            serializer = self.serializer_class(all_emp, many=True)
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message':'Sucessfully fetched Data',
                'users': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        
        employee_data = Employee.objects.all()
        serializer = self.serializer_class(employee_data, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message':'Sucessfully fetched All Employes Data',
            'users': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        employee_data = Employee.objects.get(id = id)
        serializer = EmployeeSerializer(employee_data, data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message':'Sucessfully Updated Employees Data.',
            'users': serializer.data
        }
            return Response(response,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None, format=None):
        if id is None:  
            employee_data = Employee.objects.all()
            employee_data.delete()
            return Response({'msg':'All Employee deleted..!'},status=status.HTTP_200_OK)    
        else:
            try:
                employee_data = Employee.objects.get(id=id)
                employee_data.delete()
                return Response({'msg':'Employee deleted..!'},status=status.HTTP_200_OK)
            except:
                return Response({'msg':'Id does not exists!'}, status=status.HTTP_400_BAD_REQUEST)  
