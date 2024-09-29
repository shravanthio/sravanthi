# views.py
def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query) | Product.objects.filter(description__icontains=query)
    return render(request, 'search_results.html', {'products': products})
