from django.shortcuts import render, get_object_or_404
from .models import Product, Order, Customer

# Homepage View
def homepage(request):
    new_arrivals = Product.objects.filter(category='New Arrivals')[:3]
    bestsellers = Product.objects.filter(category='Bestsellers')[:3]
    discounts = Product.objects.filter(category='Discounts')[:3]

    return render(request, 'homepage.html', {
        'new_arrivals': new_arrivals,
        'bestsellers': bestsellers,
        'discounts': discounts
    })

# Customer Dashboard View
def customer_dashboard(request):
    customer = Customer.objects.first()  # Placeholder for logged-in user
    orders = Order.objects.filter(customer=customer)

    return render(request, 'customer_dashboard.html', {
        'customer': customer,
        'orders': orders
    })

# Order Tracking View
def order_tracking(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_tracking.html', {'order': order})

# Admin Dashboard View
def admin_dashboard(request):
    products = Product.objects.all()
    orders = Order.objects.all()

    return render(request, 'admin_dashboard.html', {
        'products': products,
        'orders': orders
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})