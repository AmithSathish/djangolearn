from django.shortcuts import render
from django.http import HttpResponse
# from .models import detail
from .models import student
# Create your views here.
def page1(request):
    return HttpResponse("HELLO WORLD")
def page2(request):
    return HttpResponse("WELCOME")
def page_html(request):
    string = "Welcome to Rogersoft"
    l = ["PYTHON FULLSTACK","FLUTTER","JAVA","SOFTWARE TESTING","MERN STACK","REACT"]
    return render(request,'index.html', {'k1':string, "l1":l})
# def page_tb(request):
#     p1 = detail()
#     p1.id = 1
#     p1.name = "Akhil"
#     p1.email="akihil@gmail.com"
#     p1.pincode=679313
#     p2 = detail()
#     p2.id=2
#     p2.name="Abhilash"
#     p2.email="alibai@gmail.com"
#     p2.pincode=679121
#     p3 = detail()
#     p3.id=3
#     p3.name="Shijubal"
#     p3.email="boche@gmail.com"
#     p3.pincode=679313
#     p4 = detail()
#     p4.id=4
#     p4.name="Amith"
#     p4.email="amith@gmail.com"
#     p4.pincode=679303
#     l = [p1,p2,p3,p4]
#     return render(request,"table.html",{"details":l})
def form(request):
    if request.method == "POST":
        number1 = request.POST['num1']
        number2 = request.POST['num2']
        if 'add' in request.POST:
            result = int(number1) + int(number2)
            return render(request, "form.html", {'OUTPUT': result})

    return render(request,"form.html")


def form1(request):
    if request.method=="POST":
        if request.POST.get("name1") and request.POST.get("name2"):
            formdata=student()
            formdata.name=request.POST.get("name1")
            formdata.adress=request.POST.get("name2")
            formdata.save()
            # return render(request,'form1.html')
            tabledata = student.objects.all()
            return render(request, "form1.html", {"key": tabledata})
    tabledata=student.objects.all()
    return render(request,"form1.html",{"key": tabledata})