from django.urls import path
from .views import AuthorsListView, AuthorReteriveDeleteView

urlpatterns = [
    path('<slug:username>/', AuthorReteriveDeleteView.as_view(), name='detail__destroy_user'),
    path('', AuthorsListView.as_view(), name='list_users')
]