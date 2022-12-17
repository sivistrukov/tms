from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.accounts.urls')),
    path('', RedirectView.as_view(pattern_name='counterparties:list')),
    path('counterparties/', include('apps.counterparties.urls',
                                    namespace='counterparties')),
    path('assignments/', include('apps.assignments.urls',
                                 namespace='assignments')),
    path('shippings/', include('apps.shipping.urls',
                               namespace='shipping')),
    path('drivers/', include('apps.drivers.urls',
                             namespace='drivers')),
]
