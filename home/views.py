from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from . models import Todo
from . forms import TodoForm

# Create your views here.
def home(request):
        # https://docs.djangoproject.com/en/3.2/topics/db/examples/one_to_one/
    all_items = Todo.objects.all()
    # progress_items = Todo.objects.get('progress')

    return render(request, 'index.html', {'all_items': all_items })

def create_item(request):
    if request.method == "POST":
        name = request.POST['name']
        desc = request.POST['desc']
        complete_in = request.POST['complete_in']
        progress = request.POST['progress']

        form = Todo(name=name, des=desc, complete_in=int(complete_in), progress=progress)
        form.save()    
    return redirect('/')    


    return render(request,'index.html',{'form':form})  


def get_items(request, id):
    tasks = Todo.objects.get(id=id)

    return render(request, 'update.html', {'tasks': tasks})    


def update_task(request, id):

    task = Todo.objects.filter(id=id)
    
    # create object of form
    # form = TodoForm(request.POST, instance=task)
      
    # check if form data is valid
    if request.method == "POST":
        updated_name = request.POST['update_name']
        update_des = request.POST['update_desc']
        update_complete_in = request.POST['update_complete_in']
        
        task.update(name=updated_name, des=update_des, complete_in=update_complete_in)

    # if form.is_valid():
    #     # save the form data to model
    #     form.save()
        return redirect("/")
  
    # context['form']= form

    return render(request, 'update.html', {'task': task})  




def destroy(request, id):  
    
    task = Todo.objects.get(id=id)  
    print(task)
    task.delete()  
    return redirect("/")
    # return render(request, "index.html")      