from django.urls import include, path
from . import views

# login_patterns = [
#     path('normal/', views.login, name='login'),
# ]

urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    # path('login/', include(login_patterns)),

    #일반 로그인, 회원가입
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]