from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductCreateForm, RawProductForm


# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj,
    }

    return render(request=request, template_name="product/detail.html", context=context)

def dynamic_lookup_view(request, id):
    # Raise error 404 if not found
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)

    # Alternatively
    # try:
    #     obj = Product.objects.get(id=id)
    # except:
    #     raise Http404
    
    context = {
        "object": obj
    }

    return render(request=request, template_name="product/detail.html", context=context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect("../../")

    context = {
        "object": obj
    }

    return render(request=request, template_name="product/delete.html", context=context)      

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request=request, template_name="product/list.html", context=context)  

# model form
def product_create_view(request):
    intitial_data = {
        "title": "defualt_title",
        "description": "default_des"
    }

    form = ProductCreateForm(request.POST or None, initial=intitial_data)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()

    context = {
        "form": form,
    }

    return render(request=request, template_name="product/create.html", context=context)

# Raw HTML form
# def product_create_view(request):
#     print(request.GET)
#     print(request.POST)
    
#     if request.method == "POST":
#         title = request.POST.get('title')
#         print(title)

#     context = {}
#     return render(request=request, template_name="product/create.html", context=context)

# Pure django form
# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)

#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
 
#     context = {
#         "form": form
#     }

#     return render(request=request, template_name="product/create.html", context=context)