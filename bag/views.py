from django.shortcuts import render


def view_bag(request):
    """ A view to render the bag content page """

    return render(request, 'bag/bag.html')
