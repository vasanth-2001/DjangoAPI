from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import AuthorViewSet
# from .import views
router =DefaultRouter()
router.register('',AuthorViewSet,basename='author')
# router.register('auhtors',AuthorViewSet,basename='author')
app_name='author'

urlpatterns = [
    # path('api/',include(router.urls)),
    path('',include(router.urls)),
    # path('list/',views.list)    
]
