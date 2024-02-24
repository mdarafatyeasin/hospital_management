from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

# write your urls here
router = DefaultRouter() # router toiri kora hoyeche

router.register('specialization', views.SpecializationViewsets) #router er antena
router.register('designation', views.DesignationViewsets) #router er antena
router.register('available_time', views.AvailableTimeViewsets) #router er antena
router.register('doctor', views.DoctorViewsets) #router er antena
router.register('review', views.ReviewViewsets) #router er antena

urlpatterns = [
    path('', include(router.urls))
]
