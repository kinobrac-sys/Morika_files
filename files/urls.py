from django.urls import path
from .views import FileListView, FileDetailView, FileCreateView, FileUpdateView, FileDeleteView

urlpatterns = [
    path('', FileListView.as_view(), name='file_list'),
    path('<int:pk>/', FileDetailView.as_view(), name='file_detail'),
    path('create/', FileCreateView.as_view(), name='file_create'),
    path('<int:pk>/update/', FileUpdateView.as_view(), name='file_update'),
    path('<int:pk>/delete/', FileDeleteView.as_view(), name='file_delete'),
]