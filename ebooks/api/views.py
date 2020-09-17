from rest_framework.generics import (GenericAPIView, ListCreateAPIView, 
                                    RetrieveUpdateDestroyAPIView, CreateAPIView, get_object_or_404)
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer


class EbookListCreateAPIView(ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

class EbookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

class ReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        id = self.kwargs.get("id")
        ebook = get_object_or_404(Ebook, pk=id)
        serializer.save(ebook=ebook)

class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer




# class EbookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)