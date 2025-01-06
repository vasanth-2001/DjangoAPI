from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import BookViewSet
# from .import views
router =DefaultRouter()
router.register('',BookViewSet,basename='book')
app_name='book'

urlpatterns = [
    path('',include(router.urls)),
    # path('list/',views.list)    
]
