from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.read, name="home"),
    path('create/', views.create, name="create"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('detail/<int:pk>', views.detail, name="detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)