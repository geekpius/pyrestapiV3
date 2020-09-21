from django.urls import path, re_path
from ebooks.api.views import EbookListCreateAPIView, EbookRetrieveUpdateDestroyAPIView, ReviewCreateAPIView, ReviewRetrieveUpdateDestroyAPIView

app_name = 'ebooks'

urlpatterns = [
    path('ebooks', EbookListCreateAPIView.as_view(), name="list_create"),
    path('ebooks/<int:pk>', EbookRetrieveUpdateDestroyAPIView.as_view(), name="retrieve_update_destroy"),
    path('ebooks/<int:id>/reviews', ReviewCreateAPIView.as_view(), name="review_create"),
    path('ebooks/reviews/<int:pk>', ReviewRetrieveUpdateDestroyAPIView.as_view(), name="review_retrieve_update_destroy"),
]