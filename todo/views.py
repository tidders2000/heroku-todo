
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import item
from .forms import ItemForm
# Create your views here.

def get_todo_list(request):
    results=item.objects.all()
    return render(request, "todo_list.html", {'items':results})

def create_an_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    
    else:
        form = ItemForm()

    return render(request, "item_form.html", {'form': form})
    
def edit_an_item(request, id):
    Item = get_object_or_404(item, pk=id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=Item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    
    form=ItemForm(instance=Item)
    return render(request, "item_form.html", {'form': form})


def toggle_status(request, id):
    Item = get_object_or_404(item, pk=id)
    Item.done=not Item.done
    Item.save()
    return redirect(get_todo_list)
    