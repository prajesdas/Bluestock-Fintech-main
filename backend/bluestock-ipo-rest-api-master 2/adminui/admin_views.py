# admin_views.py
from django.contrib.admin.models import LogEntry
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from ipoApi.models import IpoInfo

class IPOContextMixin:
    def get_ipo_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['log_entries'] = LogEntry.objects.all()
        context['total_ipos'] = IpoInfo.objects.count()
        context['ipos_in_loss'] = IpoInfo.objects.filter(gain=False).count()
        context['ipos_in_gain'] = IpoInfo.objects.filter(gain=True).count()
        context['upcoming_ipos'] = IpoInfo.objects.filter(status='Coming')
        context['new_listed_ipos'] = IpoInfo.objects.filter(status='New Listed')
        context['ongoing_ipos'] = IpoInfo.objects.filter(status='Ongoing')
        context['nse_bse_ipo_count'] = IpoInfo.objects.filter(exchange__in=['NSE', 'BSE']).count()
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminPreferencesView(IPOContextMixin, TemplateView):
    template_name = 'admin/preferences/dashboard.html'

    def get_context_data(self, **kwargs):
        context = self.get_ipo_context_data(**kwargs)
        return context

@method_decorator(staff_member_required, name='dispatch')
class AdminIndexView(IPOContextMixin, TemplateView):
    template_name = 'admin/index.html'

    def get_context_data(self, **kwargs):
        context = self.get_ipo_context_data(**kwargs)
        return context