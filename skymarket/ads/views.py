import rest_framework.decorators
from rest_framework import pagination, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.permissions import IsOwnerOrAdmin
from ads.serializers import AdListSerializer, AdDetailSerializer, CommentAdSerializer, \
    AdCreateSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdListCreateView(viewsets.generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filterset_class = AdFilter

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AdListSerializer
        elif self.request.method == 'POST':
            return AdCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdListMeView(viewsets.generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        return Ad.objects.filter(author_id=self.request.user.pk)


class AdDetailUpdateDelete(viewsets.generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated,  IsOwnerOrAdmin]
        elif self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class CommentDetailUpdateDeleteView(viewsets.generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentAdSerializer

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs['ad_pk'])

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated,  IsOwnerOrAdmin]
        elif self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class CommentListCreateView(viewsets.generics.ListCreateAPIView):
    serializer_class = CommentAdSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.method == 'GET':
            return Comment.objects.filter(ad_id=self.kwargs['ad_pk'])

    def perform_create(self, serializer):
        ad_obj = Ad.objects.get(pk=self.kwargs['ad_pk'])
        serializer.save(author=self.request.user, ad=ad_obj)
