from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import Order
from payments.models import Payment
from payments.utils.generate_payment_link import generate_link


class PaymentRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        """
        Gera o link para pagamento e redireciona o usuário
        """
        user = self.request.user
        orders = Order.objects.filter(user=user)

        return str(generate_link(user, orders, Payment))
