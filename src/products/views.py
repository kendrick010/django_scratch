from django.shortcuts import render
from .models import Product

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj,
    }

    return render(request=request, template_name="product/detail.html", context=context)