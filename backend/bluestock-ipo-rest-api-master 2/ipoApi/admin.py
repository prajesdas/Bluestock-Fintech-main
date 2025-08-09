from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.templatetags.static import static
from .models import IpoInfo
from .forms import IPOForm

class IPOAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'price_band', 'open', 'close', 'issue_size', 'issue_type', 'listing_date', 'status_button', 'view_actions', 'delete_ipo')
    list_per_page = 5
    form = IPOForm

    fieldsets = (
        (None, {
            'fields': ('company_logo', 'company_name', 'location', 'price_band', 'open', 'close', 'issue_size', 'issue_type', 'listing_date', 'status', 'ipo_price', 'listing_price', 'listing_gain', 'cmp', 'current_return', 'rhp', 'drhp', 'gain', 'exchange')
        }),
    )

    def status_button(self, obj):
        if obj.status == 'Ongoing':
            return format_html('<button class="ongoing-button">Ongoing</button>')
        elif obj.status == 'Coming':
            return format_html('<button class="coming-button">Coming</button>')
        elif obj.status == 'New Listed':
            return format_html('<button class="new-listed-button">New Listed</button>')

    status_button.short_description = 'Status'
    status_button.allow_tags = True

    def view_actions(self, obj):
        return format_html(
            '<button class="action-button"><a id="update-button" href="{}">Update</a></button>',
            reverse('admin:ipoApi_ipoinfo_change', args=[obj.pk])
        )

    def delete_ipo(self, obj):
        edit_url = reverse('admin:ipoApi_ipoinfo_change', args=[obj.pk])
        delete_url = reverse('admin:ipoApi_ipoinfo_delete', args=[obj.pk])
        edit_icon = static('ipo/assets/img/view.svg')
        delete_icon = static('ipo/assets/img/delete.svg')

        return format_html(
            '<a href="{}"><img src="{}" alt="Delete" height="18"></a> '
            '<a href="{}"><img src="{}" alt="Edit" height="18"></a>',
            delete_url, delete_icon, edit_url, edit_icon
        )
    delete_ipo.short_description = 'Delete/View'
    delete_ipo.allow_tags = True

    def save_model(self, request, obj, form, change):
        # Handle logo deletion
        if not obj.company_logo and obj.pk:
            old_logo = IpoInfo.objects.get(pk=obj.pk).company_logo
            if old_logo:
                old_logo.delete(save=False)
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        # Delete the logo file
        if obj.company_logo:
            obj.company_logo.delete(save=False)
        super().delete_model(request, obj)

admin.site.register(IpoInfo, IPOAdmin)
