from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import ChefViewSet
# from .import views
router =DefaultRouter()
router.register('',ChefViewSet,basename='Chef')
app_name='Chef'

urlpatterns = [
    path('',include(router.urls)),
]
