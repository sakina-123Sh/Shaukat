from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status ,viewsets

from .models import EmployeeTable, TimingCreateTable
from .serializers import EmpSerializer, TimingCreateTableSerializer


class EmployeeTableViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTable.objects.all()
    serializer_class = EmpSerializer

    #for adding the timing in EmployeeTable :

    @action(detail=False,methods=['post'])
    def add_date_to_EmployeeTable(self,request):
        try:
            data = request.data
            serializer = TimingCreateTableSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({

                   'status': True,
                   'msg': 'Success data',
                   'data': serializer.data
                })
            return Response({
               'status': False,
               'msg': 'invalid data!!',
               'data': serializer.errors

            })
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'msg': 'Something went wrong',

            })

    @action(detail=False, methods=['GET'])
    def get_date_to_EmployeeTable(self, request):
        obj = TimingCreateTable.objects.all()
        serializer = TimingCreateTableSerializer(obj, many=True)
        return Response({
            'status':True,
            'message':'Timing of Employee Table',
            'data':serializer.data
        })








@api_view(['GET','POST','PATCH'])
def home(request):

    if request.method == 'GET':
        return Response({
            'name': 'Shaukat',
            'Message': 'Yes! Django is ready for use!!',
            'Method_Called ': 'You Called GET Method'
        })
    # return Response({
    #     'name':'Shaukat',
    #     'Message':'Yes! Django is ready for use!!'
    # })

    elif request.method == 'POST':
        return Response({
            'name': 'Shaukat',
            'Message': 'Yes! Django is ready for use!!',
            'Method_Called ': 'You Called POST Method'
        })
    elif request.method == 'PATCH':
        return Response({
            'name': 'Shaukat',
            'Message': 'Yes! Django is ready for use!!',
            'Method_Called ': 'You Called PATCH Method'
        })

    else:
        return Response({
            'name': 400,
            'Message': 'Yes! Django is ready for use!!',
            'Method_Called ': 'You Called You entered wrong Method'
        })


@api_view(['POST'])
def Post_emp(request):

    try:
        data =request.data
        serializer = EmpSerializer(data =data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)

            return Response({
                'status': True,
                'msg': 'valid data!!',
                'data': serializer.data

            })

        return Response({
            'status': False,
            'msg': 'Something went wrong',
            'data': serializer.errors
        })



    except Exception as e:
        print(e)

@api_view(['PATCH'])
def patch_Emp(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({'status':False,'msg':'uid is required','data':{}})

        obj = EmployeeTable.objects.get(uid =data.get('uid'))
        serializer = EmpSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':True,
                'msg':'sucess data',
                'data':serializer.data
            })
        return Response({
            'status':False,
            'msg':'Invalid data',
            'data':serializer.errors


        })
    except Exception as e:
        print(e)
    return Response({
        'status':False,
        'msg':'invalid uid',
        'data':{}
    })

@api_view(['GET'])
def get_emp(request):
    emp_obj = EmployeeTable.objects.all()
    serializer = EmpSerializer(emp_obj,many=True)
    return Response({
        'status':True,
        'msg':"Employee Records Fatch Succesfully!!",
        'data': serializer.data
    })


class EmployeeView(APIView):
    def get(self, request):
        emp_obj = EmployeeTable.objects.all()
        serializer = EmpSerializer(emp_obj, many=True)
        return Response({
            'status': True,
            'msg': "Employee Records Fatch Succesfully!!",
            'data': serializer.data
        })

    def post(self,request):
        try:
            data = request.data
            serializer = EmpSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)

                return Response({
                    'status': True,
                    'msg': 'valid data!!',
                    'data': serializer.data

                })

            return Response({
                'status': False,
                'msg': 'Something went wrong',
                'data': serializer.errors
            })



        except Exception as e:
            print(e)
        return Response({
            'status': 200,
            'msg': 'Yes! I am Shaukat Ali this sides!!',
            'Method Called:': 'You called the POST method'
        })

    def patch(self, request):
        try:
            data = request.data
            if not data.get('uid'):
                return Response({'status': False, 'msg': 'uid is required', 'data': {}})

            obj = EmployeeTable.objects.get(uid=data.get('uid'))
            serializer = EmpSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'msg': 'sucess data',
                    'data': serializer.data
                })
            return Response({
                'status': False,
                'msg': 'Invalid data',
                'data': serializer.errors

            })
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'msg': 'invalid uid',
            'data': {}
        })








