from django.contrib import admin
from django.urls import URLPattern, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #home page 
    path('', views.index, name="index"),
    #login
    path('login/', views.login, name="login"),
    path('Login', views.Login, name="Login"),
    #signup
    path('signup/', views.signup, name="signup"),
    path('SignUp/', views.SignUp, name="SignUp"),
    #dashboard    
    path('dashboard/', views.dashboard, name="dashboard"),
    #add
    path('add/', views.add, name="add"),
    path('Add/', views.Add, name="Add"),
    #delete
    path('delete/', views.delete, name="delete"),
    path('Delete/', views.Delete, name="Delete"),
    #update
    path('update/', views.update, name="update"),
    path('Update/', views.Update, name="Update"),
    #search
    path('search/', views.search, name="search"),
    path('Search/', views.Search, name="Search"),
    #edit
    path('edit/', views.edit, name="edit"),
    path('Edit/', views.Edit, name="Edit"),
    #forgot password
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('ForgotPassword/', views.ForgotPassword, name="ForgotPassword"),
    #redirect
    path('Redirect/', views.Redirect, name="Redirect"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)