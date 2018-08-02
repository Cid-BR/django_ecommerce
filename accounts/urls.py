from accounts import views
from checkout.views import OrderListView
from django.urls import path
from django.contrib.auth.views import login, logout


urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='registrar'),    
    path('login/', login, {'template_name':'login.html'}, name='login'),
    path('logout/', logout, {'next_page': 'index'}, name='logout'),
    path('profile/', views.UserDetailsListView.as_view(), name='profile'),
    path('profile/user/', views.UpdateUserView.as_view(), name='update_user'),
    path('profile/password/', views.UpdatePasswordView.as_view(), name='update_password'),
    path('profile/personal/', views.UpdatePersonalView.as_view(), name='update_personal'),
    path('profile/meus-pedidos', OrderListView.as_view(), name="meus_pedidos")
]
