from django.contrib import admin
from django.urls import path, include

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view


from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "ADMOB Admin"
admin.site.site_title = "ADMOB Admin"
admin.site.index_title = "Welcome to ADMOB Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('api.urls')),
    path('', TemplateView.as_view(
        template_name='index.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('api/admob/docs/', include_docs_urls(title='ADMOB API')),
    path('api/admob/schema/', get_schema_view(
        title="ADMOB API",
        description="ADMOB API Intended to Integrate with React Frontend",
        version="1.0.0"
    ), name='openapi-schema'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)