from django.urls import path
from .views import index, redirect_location, process_flow
from django.conf.urls.static import static
import sih_core.settings as settings

urlpatterns = [
    path('', index, name="index"),
    path('redirect/', redirect_location, name="redirect"),
    path('process-flow', process_flow, name="process_flow")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
