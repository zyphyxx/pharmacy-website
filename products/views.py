from django.shortcuts import render
from products.models import Product


# Create your views here.
def prod_view(request):
    query_product = Product.objects.all().order_by('price')
    search = request.GET.get('search')  # path param
    if search:
        query_product = Product.objects.filter(name__icontains=search)

    return render(request, 'main.html', {'context': query_product})
