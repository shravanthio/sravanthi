# views.py
@login_required
def place_order(request):
    # existing code
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            # Simulate payment process here
            order = Order.objects.create(
                user=request.user,
                total_price=cart_obj.total,
                shipping_address=form.cleaned_data['address']
            )
            for product in cart_obj.products.all():
                order.products.add(product)
                product.stock -= 1
                product.save()
            cart_obj.products.clear()
            return redirect('order_complete')
    return render(request, 'checkout.html', {'form': form})
