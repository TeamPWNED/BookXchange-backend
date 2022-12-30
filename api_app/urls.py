from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
        path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('v1/books', views.getBooks),
        path('v1/book', views.singlebook),
        path('v1/users', views.getUsers),
        path('v1/user/books', views.getuserbooks),
        path('v1/email', views.getEmail),
        path('v1/invite', views.getInvite),
        path('v1/transfer', views.transferCredit),
        path('v1/flagsold', views.flagsold),
        path('v1/account/register', views.RegistrationView.as_view()), 
        path('v1/account/logout', views.userlogout),
        path('v1/account/profile', views.getProfile),
        path('v1/account/profile/edit', views.updateProfile),
        path('v1/create/book', views.putBook),
        #path('v1/account/change-password', views.ChangePasswordView.as_view()),
        ]
