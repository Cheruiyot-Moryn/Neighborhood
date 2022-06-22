from django.urls import path ,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.registration, name='registration'),
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('new-hood/', views.add_neighbourhood, name='newhood'),
    path('profile/', views.profile, name='profile'),
    path('single_hood/<hood_id>', views.single_neighbourhood, name='single-hood'),
    path('join_hood/<id>', views.join_neighbourhood, name='join-hood'),
    path('leave_hood/<id>', views.leave_neighbourhood, name='leave-hood'),
    path('single_hood/<hood_id>', views.single_neighbourhood, name='single-hood'),
    path('<hood_id>/post/', views.create_post, name='post'),
    path('search/', views.search_business, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)