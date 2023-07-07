
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name = 'dashboard/auth/login.html'), name = 'user-login'),
    path('dashboard/', include('dashboard.urls')),
    #path('m-app/', include('m_app.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Administartion Titles
admin.site.site_header = "M ADMIN PANEL"
admin.site.site_title = "M"
admin.site.index_title = "We care"

