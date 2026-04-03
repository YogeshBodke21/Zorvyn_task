
from django.contrib import admin
from django.urls import path, include
from users.views import UserViewSet
from finance.views import FinancialRecordViewSet, DashboardView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path


schema_view = get_schema_view(
    openapi.Info(
        title="Zorvyn Finance API",
        default_version='v1',
        description="API documentation for finance dashboard backend",
        contact=openapi.Contact(email="your@email.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()
router.register('users', UserViewSet)
router.register('records', FinancialRecordViewSet, basename='records')


urlpatterns = [
    path('admin/', admin.site.urls),
    # JWT login
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),

    path('api/', include(router.urls)),
    path('api/dashboard/', DashboardView.as_view()),

    # Swagger UI
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0)),

    # Redoc UI (optional but impressive)
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0)),
]
