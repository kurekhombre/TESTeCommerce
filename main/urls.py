from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),
    path('category-list', views.category_list, name='category-list'),
    path('brand-list', views.brand_list, name='brand-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)