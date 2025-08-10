from django.conf import settings
from django.shortcuts import redirect
from django.urls import path, include
from . import views
from django.conf.urls.static import static
urlpatterns=[
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.another_function, name='dashboard'),
    path('',views.myfunctioncall, name="home"),
    path('add-notebook/', views.add_notebook, name='add_notebook'),
    path('notebooks/', views.notebook_list, name="notebook_list"),
    path('notebook/<int:pk>/', views.notebook_detail, name='notebook_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)