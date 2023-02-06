from django.shortcuts import render, redirect  
from school.forms import Form1AForm
from school.models import Form1A  
 
def school(request):  
    if request.method == "POST":   
        print=("hello")
        form = Form1AForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                print=("school is saved" )
                return redirect('/show')  
            except:  
                pass  
    else:   
        print=("byee")
        form = Form1AForm()  
    return render(request,'index.html',{'form':form})  


def show(request):  
    form1As= Form1A.objects.all()  
    return render(request,"show.html",{'form1As':form1As})  


def edit(request, id):  
    form1A = Form1A.objects.get(id=id)  
    return render(request,'edit.html', {'form1A':form1A})  


def update(request, id):  
    form1A= Form1A.objects.get(id=id)  
    form = Form1A(request.POST, instance = school)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'form1A': form1A})  


def destroy(request, id):  
    form1A = Form1A.objects.get(id=id)  
    form1A.delete()
    return redirect("/show")
