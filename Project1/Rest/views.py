# from django.shortcuts import render,get_object_or_404
# from .models import Category,Product

# def list_product(request,category_slug=None):
#     category=None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request,
#     '')
