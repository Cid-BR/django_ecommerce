from accounts import views
from django.urls import path
from django.contrib.auth.views import login, logout


urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='registrar'),    
    path('login/', login, {'template_name':'login.html'}, name='login'),
    path('logout/', logout, {'next_page': 'index'}, name='logout'),
    path('profile/', views.UserDetailsListView.as_view(), name='profile'),
]
