from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.conf.urls import include

urlpatterns = [
	path('snippets/',views.SnippetList.as_view(),name='snippet-list'),
	path('snippets/<int:pk>/',views.SnippetDetail.as_view(),name='snippet-detail'),
	path('users/', views.UserList.as_view(),name='user-list'),
	path('users/<int:pk>/', views.UserDetail.as_view(),name='user-detail'),
	path('api-auth/', include('rest_framework.urls')),
	path('', views.api_root),

]

urlpatterns = format_suffix_patterns(urlpatterns)