from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawproductForm

# Create your views here.
from .models import Product


'''def product_create_view(request):
    my_form = RawproductForm()
    if request.method == 'POST':
        my_form = RawproductForm(request.POST)
        if my_form.is_valid():
            # now the data is good
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)

    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context)'''

def product_create_view(request):
    form = ProductForm(request.POST or None)
    print(request.POST.get('title'))
    if form.is_valid():
         form.save()
         form = ProductForm()


    
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context) 

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.description
    }

    return render(request, "products/product_detail.html", context) 



def dynamic_lookup_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    context = {
        "object":obj
    }
    return render (request,"products/product_detail.html",context)


def product_delete_view(request,my_id):
    obj = get_object_or_404(Product, id=my_id)
    #POST DELETE THE OBJET #NOT GET DELETE
    if request.method == "POST":
        #confirming delete
        obj.delete()
        return redirect('../../')

    context = {
        "object":obj
    }
    return render (request,"products/product_delete.html",context)


def product_list_view(request):
    queryset = Product.objects.all() #list of objects
    context ={
        "object_list": queryset
    }
    return render(request,"products/product_list.html",context)
