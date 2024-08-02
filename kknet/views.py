from django.shortcuts import redirect, render

# Create your views here.


def ice_cream_main(request):
    return redirect('/icecream')

def ice_cream_list(request):
    return render(request, 'ice_cream_list.html', {

    })

def review_list(request):
    images = Ice.objects.all()
    image_url_prefix = '/static/images/'
    return render(request, 'review_list.html', {'images': images, 'image_url_prefix': image_url_prefix})

def search_view(request):
    category = request.GET.get('category', 'all')
    search_query = request.GET.get('search', '')

    if category == 'all':
        if search_query:
            images = Ice.objects.filter(name__icontains=search_query)
        else:
            images = Ice.objects.all()
    else:
        if search_query:
            images = Ice.objects.filter(category=category, name__icontains=search_query)
        else:
            images = Ice.objects.filter(category=category)

    image_url_prefix = "/static/images/"

    return render(request, 'review_list.html', {
        'images': images,
        'image_url_prefix': image_url_prefix,
        'selected_category': category,
        'search_query': search_query,
    })