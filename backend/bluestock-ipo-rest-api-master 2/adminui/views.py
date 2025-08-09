from django.shortcuts import render
from ipoApi.models import IpoInfo
from django.contrib.auth.decorators import login_required
from datetime import date
def ipo_subscription(request):
    return render(request, 'admin/iposubscription.html')

def ipo_allotment(request):
    return render(request, 'admin/ipoallotment.html')

@login_required
def index(request):
    today = date.today()
    start_date = date(2024, 1, 1)
    
    upcoming_ipos = IpoInfo.objects.filter(status='Upcoming', listing_date__gte=today)
    new_listed_ipos = IpoInfo.objects.filter(status='New Listed', listing_date__gte=start_date)
    ongoing_ipos = IpoInfo.objects.filter(status='Ongoing')
    
    nse_bse_ipo_count = IpoInfo.objects.filter(exchange__in=['NSE', 'BSE']).count()
    ipos_in_gain = IpoInfo.objects.filter(gain=True).count()
    ipos_in_loss = IpoInfo.objects.filter(gain=False).count()
    total_ipos = IpoInfo.objects.all().count()

   
    
    # Fallback to username if full name is not available
    user_name = request.user.get_full_name() or request.user.username
    
  
    context = {
        'upcoming_ipos': upcoming_ipos,
        'new_listed_ipos': new_listed_ipos,
        'ongoing_ipos': ongoing_ipos,
        'nse_bse_ipo_count': nse_bse_ipo_count,
        'ipos_in_gain': ipos_in_gain,
        'ipos_in_loss': ipos_in_loss,
        'total_ipos': total_ipos,
        'user_name': user_name,
    }
    return render(request, 'admin/preferences/dashboard.html', context)
