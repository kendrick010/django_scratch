from django.shortcuts import render
from .models import Product
from .forms import ProductCreateForm

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj,
    }

    return render(request=request, template_name="product/detail.html", context=context)

# def product_create_view(request):
#     form = ProductCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductCreateForm()

#     context = {
#         "form": form,
#     }

#     return render(request=request, template_name="product/create.html", context=context)

def product_create_view(request):
    print(request.GET)
    print(request.POST)
    
    if request.method == "POST":
        title = request.POST.get('title')
        print(title)

    context = {}
    return render(request=request, template_name="product/create.html", context=context)