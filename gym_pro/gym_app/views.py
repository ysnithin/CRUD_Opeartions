from django.shortcuts import render
import json
from .models import Emmployer
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializer import EmpSerializer
# Create your views here.

@csrf_exempt
def reg_user(req):
    user_data=json.loads(req.body)
    new_user=Emmployer.objects.create(emp_id=user_data["emp_id"],emp_name=user_data["emp_name"],emp_email=user_data["emp_email"],emp_mob=user_data["emp_mob"])
    return HttpResponse("user created")



def all_users(req):

            # without serializer
    # all_users_data=Emmployer.objects.all().values()
    # l=[]
    # for i in all_users_data:
    #     l.append(i)
    # return JsonResponse({"data":l})

    data=Emmployer.objects.all()
    all_users=EmpSerializer(data,many=True)
    return JsonResponse({"data":all_users.data})

@csrf_exempt
def update_user(req,id):
    try:
        single_user=Emmployer.objects.get(emp_id=id)
        user_data=json.loads(req.body)
        serializer=EmpSerializer(single_user,data=user_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("user updated")
        else:
            return HttpResponse("invalid data")
    except:
        return HttpResponse("user not found")
    
@csrf_exempt
def delete_user(req,id):
    try:
        single_user=Emmployer.objects.get(emp_id=id)
        single_user.delete()    
        return HttpResponse("user deleted")
    except:
        return HttpResponse("user not found")


