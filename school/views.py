from django.shortcuts import render, redirect
from school.forms import Form1AForm
from school.models import Form1A

def school(request):
    if request.method == "POST":
        form = Form1AForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            print(form.errors)
    else:
        form = Form1AForm()
    return render(request,'index.html',{'form':form})


def show(request):
    form1As= Form1A.objects.all()
    print(form1As)
    return render(request,"show.html",{'form1As':form1As})


# def edit(request, id):
#     form1A = Form1A.objects.get(id=id)
#     return render(request,'edit.html', {'form1A':form1A})

def edit(request, id):
    instance = Form1A.objects.get(id=id)

    form = Form1AForm(request.POST, instance=instance)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print('form edited')
            return redirect('show')
        else:
            for field in form:
                if field.errors:
                    print("Error in field '{}': {}".format(field.name, field.errors))

    else:
        form = Form1AForm(instance=instance)

    context = {'form': form}
    return render(request, 'edit.html', context)



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
