from django.views.generic import TemplateView

__all__ = ['Home']


class Home(TemplateView):
    template_name = 'home/dashbord.html'

    def get_context_data(self, **kwargs):
        from datetime import datetime
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio'
        context['today'] = datetime.now()
        context['account_number'] = user.account_number
        context['countable_balance'] = user.countable_balance
        context['balance_available_current_account'] = user.balance_available_current_account
        context['available_credit_line_balance'] = user.available_credit_line_balance
        context['total_abonos'] = user.total_abonos
        context['total_charges'] = user.total_charges

        return context
