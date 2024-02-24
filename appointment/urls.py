from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

# write your urls
router = DefaultRouter()

router.register('all', views.appointmentViewsets)

urlpatterns = [
    path('', include(router.urls))
]
