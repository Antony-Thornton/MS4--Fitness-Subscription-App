# Makes the contents available to the whole application. Needs to be added to the templates variable in the settings.py on the project level.

from decimal import Decimal
from django.conf import settings

def cart_contents(request):
    
    cart_items = []
    total = 0
    product_count = 0  
    
    if total == 0:
        delivery = 0
    else:
        delivery = total * Decimal(settigns.STANDARD_DELIVERY_PERCENTAGE/100)

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery':delivery,
        'grand_total': grand_total,
    }

    return context
    