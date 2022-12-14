from django.urls import path
from .views import BookListView, BookDetailView, BookUpdateView, BookDeleteView, BookCreateView

urlpatterns = [
    path('', BookListView.as_view(), name="book_list"),
    path('<int:pk>/', BookDetailView.as_view(), name="book_detail"),
    path('<int:pk>/update/', BookUpdateView.as_view(), name="book_update"),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name="book_delete"),
    path('create/', BookCreateView.as_view(), name="book_create")
]