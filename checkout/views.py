from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        # Prevent people to type checkout in url
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JBgEgKtcGNIskVi6Ev8w0GAmZ6JNxxUcAs6Ed7yTHBhDlkJioWaelYcv0CmYUHHNOZyQo4YZGy48DiV06x5CEYN00DVBapr2Y',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
