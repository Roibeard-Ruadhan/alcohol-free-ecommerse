from django.apps import AppConfig
""" Checkout app """

class CheckoutConfig(AppConfig):
    """ Checkout app """
    name = 'checkout'

    def ready(self):
        import checkout.signals