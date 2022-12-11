from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.accounts.urls')),
    path('counterparties/', include('apps.counterparties.urls',
                                    namespace='counterparties')),
    path('', RedirectView.as_view(pattern_name='counterparties:list')),
]
