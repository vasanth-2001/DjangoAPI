from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import DishViewSet
# from .import views
router =DefaultRouter()
router.register('',DishViewSet,basename='Dish')
app_name='Dish'

urlpatterns = [
    path('',include(router.urls)),
]
