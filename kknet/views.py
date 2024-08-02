from django.shortcuts import redirect, render

# Create your views here.


def ice_cream_main(request):
    return redirect('/icecream')

def ice_cream_list(request):
    return render(request, 'ice_cream_list.html', {

    })