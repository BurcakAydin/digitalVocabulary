from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/profiles/', include('profiles.urls')),
    path('api/vocabularies/', include('vocabularies.urls')),
    path('api/exercises/', include('exercises.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


