from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#router.register(r'tasks', views.TaskViewSet, base_name='tasks')
router.register(r'calculo', views.PagoViewSet, base_name='pago')

urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^calculo/$', views.CalculoView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^task/', views.TaskViewSet.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

