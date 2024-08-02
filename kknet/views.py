from django.shortcuts import get_object_or_404, redirect, render

from kknet.models import Icecream
from django.db.models import Q
# Create your views here.


def ice_cream_main(request):
    return redirect('/icecream')

def ice_cream_list(request):
    query = request.GET.get('query', '')
    category = request.GET.get('category', '')
    
    ice_creams = Icecream.objects.all()
    
    if category:
        ice_creams = ice_creams.filter(category=category)
        
    if query:
        ice_creams = ice_creams.filter(
            Q(name__icontains=query) |
            Q(manufacturer__icontains=query)  
        )
        
    categories = category.objects.all()


    return render(request, 'board/ice_cream_list.html', {
        'ice_creams': ice_creams,
        'categories': categories,
        'query': query,
        'selected_category': category,
    })
    
    

def ice(request):
    images = Icecream.objects.all()
    image_url_prefix = '/static/images/'
    return render(request, 'review_list.html', {'images': images, 'image_url_prefix': image_url_prefix})

def search_view(request):
    category = request.GET.get('category', 'all')
    search_query = request.GET.get('search', '')

    if category == 'all':
        if search_query:
            images = Icecream.objects.filter(name__icontains=search_query)
        else:
            images = Icecream.objects.all()
    else:
        if search_query:
            images = Icecream.objects.filter(category=category, name__icontains=search_query)
        else:
            images = Icecream.objects.filter(category=category)

    image_url_prefix = "/static/images/"

    return render(request, 'review_list.html', {
        'images': images,
        'image_url_prefix': image_url_prefix,
        'selected_category': category,
        'search_query': search_query,
    })
    
def ice_cream_detail(request, pk):
    ice_cream = get_object_or_404(Icecream, pk=pk)
    return render(request, 'board/ice_cream_detail.html', {
        'ice_cream': ice_cream,
    })
    
def ice_cream_reviews(request, pk):
        ice_cream = get_object_or_404(Icecream, pk=pk)
        reviews = ice_cream.reviews.all()
        return render(request, 'ice_cream_reviews.html', {
            'ice_cream': ice_cream,
            'reviews': reviews,
        })

def ice_cream_information(request, pk):
    ice_cream = get_object_or_404(Icecream, pk=pk)
    information = ice_cream.information.all()
    return render(request, 'ice_cream_information.html', {
        'ice_cream': ice_cream,
        'information': information,
    })
    
def add_review(request, pk):