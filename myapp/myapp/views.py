from django.shortcuts import render

# Create your views here.



from django.http import HttpResponse
def home(request):
   isactive=True
   if request.method=='POST':
      check=request.POST.get("check1") #POST['check'] can aslo use
      print(check)
      if check is None: isactive=False
      else: isactive=True
      print("test")
 
 
 
   name="code"
   list_programs=["wap1","wap2","wap3"]
   student={
    'student_name':"yeah",
        'student_area':"yeah1",
        'student_course':"Java"   
           
    }
   data={
        'name':name,
        'isactive':isactive,
        'list_programs':list_programs,
        'student_data':student 
    }
    #return HttpResponse("<h1> hello this <h1>")

   return render(request,"home.html",data)




def about(request):
    print("test")
    return render(request,"about.html",{})


def services(request):
    print("test")
    return render(request,"services.html",{})

