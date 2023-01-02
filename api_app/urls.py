from django.urls import path, re_path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="BookXchange API",
        default_version='v1',
        description="Welcome to BookXchange",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
        path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('v1/books', views.getBooks, name='get_all_books'),
        path('v1/book', views.singlebook, name='get_single_book'),
        path('v1/users', views.getUsers, name='get_all_users'),
        path('v1/user/books', views.getuserbooks, name='get_user_books'),
        path('v1/email', views.getEmail, name='invite_list_endpoint'),
        path('v1/invite', views.getInvite, name='invite_to_bookxchange'),
        path('v1/transfer', views.transferCredit, name='credit_transfer'),
        path('v1/flagsold', views.flagsold, name='flag_as_sold'),
        path('v1/account/register', views.RegistrationView.as_view(), name='register_user'), 
        path('v1/account/logout', views.userlogout, name='logout_user'),
        path('v1/account/profile', views.getProfile, name='get_user_profile'),
        path('v1/account/profile/edit', views.updateProfile, name='edit_user_profile'),
        path('v1/create/book', views.putBook, name='create_book'),
        re_path(r'^v1(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),  
        path('v1/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  
        path('v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
        #path('v1/account/change-password', views.ChangePasswordView.as_view()),
        ]
