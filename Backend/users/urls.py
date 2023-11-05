from .views import CreateUserView,BlackListToken,TestView
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("create_user/",CreateUserView.as_view(),name="createuser"),
    path("api-auth/",include("rest_framework.urls",namespace="rest_framework"),name = "rest_framework"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', BlackListToken.as_view(),
         name='blacklist'),
    path('test/',TestView.as_view(),name='testview'),

]