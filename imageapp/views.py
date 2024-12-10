from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
import os

# Display the add product page
def index(request):
    return render(request, "add_product.html")

# Add a new product
def add_product(request):
    if request.method == "POST":
        pname = request.POST.get('p_name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        image = request.FILES.get('file')

        product = Product(product_name=pname, quantity=quantity, price=price, image=image)
        product.save()
        return redirect('show_product')
    return render(request, "add_product.html")

# Display all products
def show_product(request):
    products = Product.objects.all()
    return render(request, 'show_product.html', {'products': products})

# Display the edit product page
def editpage(request, pk):
    prdts = Product.objects.get(id=pk)
    return render(request, 'edit_product.html', {'prdts': prdts})

# Edit an existing product
def edit_product(request, pk):
    if request.method == 'POST':
        prdts = Product.objects.get(id=pk)
        prdts.product_name = request.POST.get('pname')
        prdts.price = request.POST.get('price')
        prdts.quantity = request.POST.get('qty')
        if 'file' in request.FILES:
            if prdts.image and os.path.isfile(prdts.image.path):
                os.remove(prdts.image.path)
            prdts.image = request.FILES['file']
        prdts.save()
        return redirect('show_product')
    return render(request, 'edit_product.html')



def edit_product(request, pk):
    if request.method == 'POST':
        # Get the existing product
        prdts = get_object_or_404(Product, id=pk)

        # Update text fields
        prdts.product_name = request.POST.get('pname')
        prdts.price = request.POST.get('price')
        prdts.quantity = request.POST.get('qty')

        # Handle the new file upload
        if 'file' in request.FILES:
            # Delete the old image if it exists
            if prdts.image and os.path.isfile(prdts.image.path):
                os.remove(prdts.image.path)
            # Assign the new image
            prdts.image = request.FILES['file']

        # Save the updated product
        prdts.save()
        return redirect('show_product')

    return render(request, 'edit.html', {'prdts': prdts})


# Delete a product
def delete(request, pk):
    p = Product.objects.get(id=pk)
    if p.image and os.path.isfile(p.image.path):
        os.remove(p.image.path)
    p.delete()
    return redirect('show_product')
