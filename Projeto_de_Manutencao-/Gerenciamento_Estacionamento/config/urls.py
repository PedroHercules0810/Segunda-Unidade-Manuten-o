"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users.api.views import UserProfileExampleViewSet
from estacionamento.api.views import ClienteViewSet
from estacionamento.api.views import VeiculoViewSet, EstacionamentoViewSet

router = SimpleRouter()


def trigger_error(request):
    #division_by_zero = 1 / 0
router.register("users", UserProfileExampleViewSet, basename="users")
router.register("estacionamento", EstacionamentoViewSet, basename="estacionamentos")
router.register("veiculo", VeiculoViewSet, basename="veiculos")
router.register("cliente", ClienteViewSet, basename="clientes")


urlpatterns = [
    path("admin/", admin.site.urls),
    path('sentry-debug/', trigger_error),
    path("api/token-auth/", views.obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]+router.urls
