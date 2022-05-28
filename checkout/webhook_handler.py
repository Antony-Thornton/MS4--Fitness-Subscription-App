from django.http import HttpResponse

class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected Webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle a payment_intent.succeeded webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook received {event["type"]}',
            status=200)
    
        def handle_payment_intent_payment_failed(self, event):
            """
            Handle a payment_intent.failed webhook from stripe
            """
            return HttpResponse(
                content=f'Payment failed: {event["type"]}',
                status=200)


