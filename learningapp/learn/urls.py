from.import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'learn'

urlpatterns = [ 
    path('create-content/', views.ContentCreateView.as_view(), name='create-content'),
    path('content-list/', views.ContentListView.as_view(), name='content-list'),
    path('content-detail/<int:pk>/', views.ContentDetailView.as_view(), name='content-detail'),
    path('content-update/<int:pk>/', views.ContentUpdateView.as_view(), name='content-update'),
    path('', views.IndexPageView.as_view(), name=''),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    