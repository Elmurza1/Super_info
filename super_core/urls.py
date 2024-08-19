"""
URL configuration for super_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from info.views import PublicationView, ContactView, client_message,  HomeView, PublicationCommentView
from django.conf.urls.static import static
from django.conf.urls.static import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18/', include('django.conf.urls.i18n')),
]
urlpatterns +=i18n_patterns(
path('home/', HomeView.as_view(), name='home-list'),
#    path('home/search/', SearchView.as_view(), name='search-home-url'),
     path('contact/', ContactView.as_view(), name='contact-list'),
     path('publication/<int:pk>', PublicationView.as_view(), name='publication-detail'),
     path('contact/client-create-contact/', client_message , name='contact-list'),
     path('publication/<int:pk>/comment/',PublicationCommentView.as_view(), name='comment-url' )
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)