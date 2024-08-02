<<<<<<< HEAD
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
        
    q = None
    
    if query :
        q = Q(name__icontains=query)
        q.add(Q(mfr__icontains=query), Q.OR)           
        
    if category and category != "all":
        q.add(Q(category=category), Q.AND)
    
    if query or (category and category != "all"):
        ice_creams = Icecream.objects.filter(q)
    else :
        ice_creams = Icecream.objects.all()
        
    print(ice_creams)

    return render(request, 'IcecreamList.html', {
        'ice_creams': ice_creams,
        'query': query,
        'selected_category': category,
    })
    
    
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
=======
# from django.shortcuts import redirect, render

# # Create your views here.


# def ice_cream_main(request):
#     return redirect('/icecream')

# def ice_cream_list(request):
#     return render(request, 'ice_cream_list.html', {

#     })

# def review_list(request):
#     images = Ice.objects.all()
#     image_url_prefix = '/static/images/'
#     return render(request, 'review_list.html', {'images': images, 'image_url_prefix': image_url_prefix})

# def search_view(request):
#     category = request.GET.get('category', 'all')
#     search_query = request.GET.get('search', '')

#     if category == 'all':
#         if search_query:
#             images = Ice.objects.filter(name__icontains=search_query)
#         else:
#             images = Ice.objects.all()
#     else:
#         if search_query:
#             images = Ice.objects.filter(category=category, name__icontains=search_query)
#         else:
#             images = Ice.objects.filter(category=category)
>>>>>>> 0be4f513babd5b97dbd7622911318d222624ff8a

#     image_url_prefix = "/static/images/"

<<<<<<< HEAD
    return render(request, 'review_list.html', {
        'images': images,
        'image_url_prefix': image_url_prefix,
        'selected_category': category,
        'search_query': search_query,
    })
    
def ice_cream_detail(request, pk):
    ice_cream = get_object_or_404(Icecream, pk=pk)
    return render(request, 'ice_cream_detail.html', {
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
    information = ice_cream.informations.all()
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
            from django.contrib.auth.hashers import make_password, check_password

             
            if content and rating and password:
                review = Review.objects.create(
                    ice_cream=ice_cream,
                    content=content,
                    rating=int(rating),
                    pw_hash=make_password(password),
                )
                review.save()
                messages.success(request, '리뷰가 성공적으로 추가되었습니다.')
            else:
                messages.error(request, '모든 필드를 입력해주세요.')
            return redirect('ice_cream_reviews', pk=pk)
        return render(request, 'ice_cream_reviews.html', {'ice_cream': ice_cream})



def add_information(request, pk):
    ice_cream = get_object_or_404(Icecream, pk=pk)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        discount_password = request.POST.get('discount_password')
        purchase_date = request.POST.get('purchase_date')
        
        if content and discount_password and purchase_date:
            from django.contrib.auth.hashers import make_password
            Discountinfo.objects.create(
                ice_cream=ice_cream,
                content=content,
                pw_hash=make_password(discount_password),
            )
            messages.success(request, '정보가 성공적으로 추가되었습니다.')
        else:
            messages.error(request, '모든 필드를 입력해주세요.')
        
        return redirect('ice_cream_information', pk=pk)
    
    return render(request, 'ice_cream_information.html', {'ice_cream': ice_cream})


def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        password = request.POST.get('password')
        from django.contrib.auth.hashers import check_password

        if check_password(password,review.pw_hash):
            review.delete()
            messages.success(request, '리뷰가 성공적으로 삭제되었습니다.')
        else:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
        return redirect('ice_cream_reviews', pk=review.ice_cream.pk)
    return render(request, 'delete_review.html', {'review': review})
=======
#     return render(request, 'review_list.html', {
#         'images': images,
#         'image_url_prefix': image_url_prefix,
#         'selected_category': category,
#         'search_query': search_query,
#     })
>>>>>>> 0be4f513babd5b97dbd7622911318d222624ff8a
