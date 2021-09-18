from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    # Access bag from session and calculating total cost
    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += item_data * product.price
        product_count += item_data
        bag_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'product': product,
        })

    # Calculating free shipping
    if total < settings.FREE_SHIPPING_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_SHIPPING_PRECENTAGE / 100)
        # Show to user how much more they need to spend for free shipping
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        delivery = 0
        free_shipping_delta = 0

    # Calculating bag total
    grand_total = delivery + total

    # everything in this context will be available in every template and app across the entire project
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
