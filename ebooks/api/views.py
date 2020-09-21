from rest_framework.generics import (GenericAPIView, ListCreateAPIView, 
                                    RetrieveUpdateDestroyAPIView, CreateAPIView, get_object_or_404)
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import (IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser)
from rest_framework.exceptions import ValidationError

from ebooks.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly
from ebooks.api.paginations import SmallSetPagination
from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer


class EbookListCreateAPIView(ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    pagination_class = SmallSetPagination
    permission_classes = [IsAdminUserOrReadOnly]


class EbookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class ReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        id = self.kwargs.get('id')
        ebook = get_object_or_404(Ebook, pk=id)
        review_author = self.request.user
        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)
        if review_queryset.exists():
            raise ValidationError('You have already reviewed this ebook')

        serializer.save(ebook=ebook, review_author=review_author)


class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]




# class EbookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)