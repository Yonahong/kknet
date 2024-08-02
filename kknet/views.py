from django.contrib import messages
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render

from kknet.models import Discountinfo, Icecream, Review
from django.db.models import Q
# Create your views here.


def ice_cream_main(request):
    return redirect('/icecreams')

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
        

    return render(request, 'IcecreamList.html', {
        'ice_creams': ice_creams,
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
        ice_cream = get_object_or_404(Icecream, pk=pk)

        if request.method == 'POST':
            content = request.POST.get('content')
            rating = request.POST.get('rating')
            password = request.POST.get('password')
            if content and rating and password:
                review = Review.objects.create(
                    ice_cream=ice_cream,
                    content=content,
                    rating=int(rating),
                    password=password,
                    created_at=timezone.now()
                )
                review.save()
                messages.success(request, '리뷰가 성공적으로 추가되었습니다.')
            else:
                messages.error(request, '모든 필드를 입력해주세요.')
            return redirect('ice_cream_reviews', pk=pk)
        return render(request, 'board/ice_cream_reviews.html', {'ice_cream': ice_cream})



def add_information(request, pk):
    ice_cream = get_object_or_404(Icecream, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        discount_password = request.POST.get('discount_password')
        purchase_date = request.POST.get('purchase_date')
        if content and discount_password and purchase_date:
            information = Discountinfo.objects.create(
                ice_cream=ice_cream,
                content=content,
                discount_password=discount_password,
                created_at=timezone.now(),
                purchase_date=purchase_date
            )
            information.save()
            messages.success(request, '정보가 성공적으로 추가되었습니다.')
        else:
            messages.error(request, '모든 필드를 입력해주세요.')
        return redirect('ice_cream_information', pk=pk)
    return render(request, 'board/ice_cream_information.html', {'ice_cream': ice_cream})


def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == review.password:
            review.delete()
            messages.success(request, '리뷰가 성공적으로 삭제되었습니다.')
        else:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
        return redirect('ice_cream_reviews', pk=review.ice_cream.pk)
    return render(request, 'board/delete_review.html', {'review': review})