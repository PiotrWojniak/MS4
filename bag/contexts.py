from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

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
