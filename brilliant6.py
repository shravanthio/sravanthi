# views.py
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            # Process order
            return redirect('order_summary')
    else:
        form = ShippingForm()
    return render(request, 'checkout.html', {'form': form})
