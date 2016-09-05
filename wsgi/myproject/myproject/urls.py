from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'calculo', views.PagoViewSet, base_name='pago')
router.register(r'impuesto', views.IsptViewSet)
router.register(r'reglas', views.ReglaViewSet)
router.register(r'constantes', views.ConstanteViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

