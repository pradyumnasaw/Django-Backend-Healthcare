from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegisterView, UserLoginView, PatientViewSet, DoctorViewSet, PatientDoctorMappingViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'mappings', PatientDoctorMappingViewSet)

urlpatterns = [
    path('auth/register/', UserRegisterView.as_view(), name='register'),
    path('auth/login/', UserLoginView.as_view(), name='login'),
    path('', include(router.urls)),
]