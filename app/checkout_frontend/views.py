from django.shortcuts import render

from checkout_frontend.app import app


class CheckoutView:

    def get(self, request):
        """Return the exchange_rate_evolution view with the neccesary data"""

        _cart_id = request.GET.get('cart_id')

        if _cart_id:
            cart = app.checkout.get_cart(_cart_id)
        else:
            cart = app.checkout.create_cart()

        return render(request, 'checkout.html', {
            'products': app.product_repository.all(),
            'offers': app.offer_repository.all(),
            'cart': cart,
            'total_amount': app.checkout.get_total_amount(cart),
        })
