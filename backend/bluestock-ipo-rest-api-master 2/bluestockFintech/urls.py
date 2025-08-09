from django.contrib import admin
from django.urls import path, include
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from adminui.admin_views import AdminPreferencesView,AdminIndexView

admin.autodiscover()
urlpatterns = [ 
     path('admin/dashboard/', AdminPreferencesView.as_view(), name='admin-preferences'),
    path('admin/', AdminIndexView.as_view(), name='admin_index'),
    path('admin/', admin.site.urls),
    path('administrator/api/v1/',include('ipoApi.urls')),
    path('api/user/',include('authUser.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








