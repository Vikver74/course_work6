from django.urls import path

from ads.views import AdListCreateView, CommentDetailUpdateDeleteView, \
    CommentListCreateView, AdListMeView, AdDetailUpdateDelete


urlpatterns = [
    path('ads/', AdListCreateView.as_view(), name='ad_list_create'),
    path('ads/<int:pk>/', AdDetailUpdateDelete.as_view(), name='ad_detail_update_delete'),
    path('ads/me/', AdListMeView.as_view(), name='ad_me_list'),
    path('ads/<int:ad_pk>/comments/', CommentListCreateView.as_view(), name='comments_list_create'),
    path('ads/<int:ad_pk>/comments/<int:pk>/', CommentDetailUpdateDeleteView.as_view(), name='comments_detail_update_delete'),
]
